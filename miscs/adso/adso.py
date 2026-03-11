#!/usr/bin/env python

from argparse import ArgumentParser
from os import path
from re import search
from requests import get, post
from sys import argv, exit
from time import sleep
from urllib.parse import urlparse, parse_qs
import logging as log
import json

CONFIG_FILE = "config.json"
EPISODES_BASE_DIR = path.join(path.dirname(__file__), "..", "..", "_episodes")

def extract_panopto_session_id(url):
    parsed = urlparse(url)
    if 'id=' in parsed.query:
        query_params = parse_qs(parsed.query)
        return query_params.get('id', [None])[0]

    match = search(r'/Sessions/([a-f0-9-]+)', parsed.path)
    if match:
        return match.group(1)

    return None

def get_panopto_access_token(server, client_id, client_secret):
    token_url = f"https://{server}/Panopto/oauth2/connect/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials",
        "scope": "api",
        "client_id": client_id,
        "client_secret": client_secret
    }

    log.info(f"Requesting OAuth2 token from {token_url}")
    response = post(token_url, headers=headers, data=data)

    if response.status_code != 200:
        log.error(f"Token request failed with status {response.status_code}")
        log.error(f"Response: {response.text}")

    response.raise_for_status()

    token_data = response.json()
    return token_data.get("access_token")

def get_panopto_session(server, session_id, access_token):
    api_url = f"https://{server}/Panopto/api/v1/sessions/{session_id}"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    log.debug(f"Fetching session data from {api_url}")
    response = get(api_url, headers=headers)
    response.raise_for_status()

    return response.json()

def get_panopto_folder_sessions(server, folder_id, access_token, limit=0):
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    all_sessions = []
    page = 0
    page_size = 50
    max_retries = 3
    consecutive_errors = 0

    while True:
        api_url = f"https://{server}/Panopto/api/v1/folders/{folder_id}/sessions"
        params = {
            "pageNumber": page,
            "maxResults": page_size
        }

        log.info(f"Fetching sessions page {page} from folder {folder_id}")

        retry_count = 0
        while retry_count < max_retries:
            response = get(api_url, headers=headers, params=params)

            if response.status_code == 500:
                retry_count += 1
                if retry_count < max_retries:
                    log.warning(f"Got 500 error on page {page}, retrying ({retry_count}/{max_retries})...")
                    sleep(2)
                    continue
                else:
                    log.error(f"Got 500 error on page {page} after {max_retries} retries")
                    consecutive_errors += 1
                    if consecutive_errors >= 3:
                        log.warning(f"Got {consecutive_errors} consecutive errors, stopping pagination")
                        return all_sessions
                    break

            response.raise_for_status()
            break

        if retry_count >= max_retries:
            page += 1
            continue

        data = response.json()
        results = data.get('Results', [])

        if not results:
            break

        consecutive_errors = 0
        all_sessions.extend(results)
        log.info(f"Retrieved {len(results)} sessions (total so far: {len(all_sessions)})")

        total_results = data.get('TotalNumberResults')
        if total_results is not None:
            log.info(f"API reports {total_results} total results")
            if len(all_sessions) >= total_results:
                break

        if len(results) < page_size or (limit > 0 and len(results) > limit):
            break

        page += 1

    return all_sessions

def extract_episode_number(session_name):
    match = search(r'Episode\s+(\d+)', session_name, )
    if match:
        episode_num = match.group(1)
        return episode_num.zfill(4)
    return None

def download_panopto_transcript(download_url):
    log.info(f"Downloading transcript from {download_url}")
    response = get(download_url)
    response.raise_for_status()
    return response.text

def generate_html_transcript(session_data, transcript_text, video_url):
    episode_num = extract_episode_number(session_data.get('Name', ''))
    if not episode_num:
        log.error(f"Could not extract episode number from session name: {session_data.get('Name')}")
        return None, None

    title = session_data.get('Name', 'Unknown Episode')
    description = session_data.get('Description', '')

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
</head>
<body>
    <article>
        <h1>{title}</h1>
        <div data-pagefind-meta="url">{video_url}</div>
        <p><a href="{video_url}">Watch Video</a></p>
        <div data-pagefind-body>
            <pre>{transcript_text}</pre>
        </div>
    </article>
</body>
</html>"""

    return episode_num, html_content

def process_session(config, session_data, video_url, force_overwrite=False):
    episode_num = extract_episode_number(session_data.get('Name', ''))
    if not episode_num:
        log.error(f"Could not extract episode number from: {session_data.get('Name')}")
        return False

    episode_dir = path.join(EPISODES_BASE_DIR, episode_num)
    if not path.exists(episode_dir):
        log.warning(f"Episode directory not found: {episode_dir}, skipping")
        return False

    output_path = path.join(episode_dir, "transcript.html")
    if path.exists(output_path) and not force_overwrite:
        log.info(f"Transcript already exists for episode {episode_num}, skipping")
        return True

    caption_url = session_data.get('Urls', {}).get('CaptionDownloadUrl')
    if not caption_url:
        log.error(f"No caption download URL found for session: {session_data.get('Name')}")
        return False

    transcript_text = download_panopto_transcript(caption_url)

    episode_num, html_content = generate_html_transcript(
        session_data,
        transcript_text,
        video_url
    )

    if not episode_num:
        log.error(f"Could not extract episode number from: {session_data.get('Name')}")
        return False

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

    log.info(f"Transcript successfully saved to {output_path}")
    return True

def check_unavailable_sessions(server, sessions, access_token):
    unavailable_urls = []
    for session in sessions:
        session_id = session.get('Id')
        viewer_url = session.get('Urls', {}).get('ViewerUrl')

        if not session_id or not viewer_url:
            continue

        try:
            get_panopto_session(server, session_id, access_token)
        except Exception as e:
            if hasattr(e, 'response') and e.response.status_code == 404:
                unavailable_urls.append(viewer_url)
            else:
                raise

    return unavailable_urls

def main(options):
    with open(CONFIG_FILE) as f:
        config = json.load(f)

    log.info("Loaded config.json")

    access_token = get_panopto_access_token(
        config['panopto_server'],
        config['panopto_client_id'],
        config['panopto_client_secret']
    )
    log.info("Successfully obtained access token")

    if options.limit > 0:
        log.debug(f"Limiting to {options.limit} sessions")

    if options.check_for_not_available:
        if options.folder_id:
            sessions = get_panopto_folder_sessions(
                config['panopto_server'],
                options.folder_id,
                access_token,
                options.limit
            )
        elif options.url_file:
            sessions = []
            with open(options.url_file, 'r') as f:
                for line in f:
                    url = line.strip()
                    if not url or url.startswith('#'):
                        continue
                    session_id = extract_panopto_session_id(url)
                    if session_id:
                        sessions.append({'Id': session_id, 'Urls': {'ViewerUrl': url}})
                    else:
                        log.warning(f"Could not extract session ID from URL: {url}")
        else:
            session_id = extract_panopto_session_id(options.vid_url)
            if not session_id:
                log.error(f"Could not extract session ID from URL: {options.vid_url}")
                return 1
            sessions = [{'Id': session_id, 'Urls': {'ViewerUrl': options.vid_url}}]

        print("Not available videos:\n")
        unavailable_urls = check_unavailable_sessions(config['panopto_server'], sessions, access_token)
        for url in unavailable_urls:
            print(url)
        return 0

    if options.folder_id:
        sessions = get_panopto_folder_sessions(
            config['panopto_server'],
            options.folder_id,
            access_token
        )

        log.info(f"Found {len(sessions)} sessions in folder")

        success_count = 0
        processed_count = 0
        for session in sessions:
            session_id = session.get('Id')
            viewer_url = session.get('Urls', {}).get('ViewerUrl')

            if not session_id or not viewer_url:
                log.warning(f"Skipping session with missing data: {session.get('Name')}")
                continue

            log.info(f"Processing: {session.get('Name')}")

            if process_session(config, session, viewer_url, options.force_overwrite):
                success_count += 1

            processed_count += 1

            if processed_count % 50 == 0:
                log.info(f"Processed {processed_count} sessions, resting for 5 seconds...")
                sleep(5)

        log.info(f"Successfully processed {success_count}/{len(sessions)} sessions")
        return 0

    else:
        session_id = extract_panopto_session_id(options.vid_url)
        if not session_id:
            log.error(f"Could not extract session ID from URL: {options.vid_url}")
            return 1

        log.info(f"Extracted session ID: {session_id}")

        session_data = get_panopto_session(
            config['panopto_server'],
            session_id,
            access_token
        )

        if process_session(config, session_data, options.vid_url, options.force_overwrite):
            return 0
        else:
            return 1



if __name__ == "__main__":
    parser = ArgumentParser()

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--vid-url",
        type=str,
        help="URL of video to download transcript for")
    group.add_argument(
        "--folder-id",
        type=str,
        help="Panopto folder ID to process all sessions from")
    group.add_argument(
        "--url-file",
        type=str,
        help="File containing list of video URLs (one per line)")

    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Print debugging messages to the console.")
    parser.add_argument(
        "--force-overwrite",
        action="store_true",
        help="Overwrite existing transcript files")
    parser.add_argument(
        "--check-for-not-available",
        action="store_true",
        help="Check if video(s) return 404s and echo URL(s) if so")
    parser.add_argument(
        "--limit",
        type=int,
        default=0,
        help="Debug tool for --folder-id that limits the number of sessions to process")

    options, extra = parser.parse_known_args(argv[1:])

    log_level = log.DEBUG if options.verbose else log.INFO
    log.basicConfig(format="%(levelname)s:  %(message)s", level=log_level)

    exit(main(options))
