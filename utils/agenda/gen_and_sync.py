import argparse
import datetime
import json
import logging
import markdown2
import os
import pywatchman
import re
import requests
import sys


def watch(options):
    logging.debug("Watching folder %s" % options.notesdir)
    client = pywatchman.client(timeout=5.0)
    query = {
        "empty_on_fresh_instance": True,
        "expression": [
            "allof",
            ["type", "f"],
            [
                "not",
                [
                    "anyof",
                    ["dirname", ".hg"],
                    ["name", ".hg", "wholename"],
                    ["dirname", ".git"],
                    ["name", ".git", "wholename"],
                ],
            ],
            [
                "match",
                "*.md"
            ],
        ],
        "fields": ["name"],
    }

    watch = client.query("watch-project", options.notesdir)
    root = watch["watch"]
    query["since"] = client.query("clock", root, {"sync_timeout": 30000})[
        "clock"
    ]

    name = "notesdir"

    client.query("subscribe", root, name, query)
    shouldRsync = False
    try:
        while True:
            try:
                client.receive()
                changed_file_data = client.getSubscription(name)
                if changed_file_data:
                    changed_files = set()
                    for data in changed_file_data:
                        for f in data.get("files", []):
                            changed_files.add(f)

                    shouldRsync = True
                    options.changed_files = changed_files
                    run(options)
                    break

            except pywatchman.SocketTimeout:
                # Let's check to see if we're still functional.
                client.query("version")
            except KeyboardInterrupt:
                logging.info("Keyboard interrupt - closing")
                break
    finally:
        client.close()

    if shouldRsync:
        sys.exit(0)
    else:
        sys.exit(1)


def run(options):
    logging.debug("Loading config from %s" % options.config)
    with open(options.config, "r") as f:
        CONFIG = json.load(f)

    logging.debug("Loading template file: %s" % options.template)
    with open(options.template, "r") as f:
        template = f.read()

    logging.debug(
        "Attempting to contact Joplin on localhost:%s" % CONFIG["JOPLIN_PORT"]
    )
    payload = {"token": CONFIG["TOKEN"], "order_by": "updated_time", "order_dir": "ASC", "fields": "id,updated_time"}
    url = "http://localhost:%s/tags/%s/notes/" % (
        CONFIG["JOPLIN_PORT"],
        CONFIG["EXPORT_TAG_ID"],
    )
    page = 1

    notes = []
    while True:
        payload["page"] = page

        response = requests.get(url, payload).json()
        notes = notes + response["items"]

        if not response["has_more"]:
            break

        page = page + 1

    notes.sort(key=lambda n: n["updated_time"], reverse=True)

    image_re = re.compile(r"\(:/([a-z0-9]*)\)", re.MULTILINE)
    episode_re = re.compile(r"Episode ([0-9]+)")

    for note in notes:
        logging.info("Considering note with ID: %s" % note["id"])
        filename = "%s.md" % note["id"]

        if options.changed_files:
            if filename not in options.changed_files:
                break
        else:
            note_updated_time = datetime.datetime.fromtimestamp(float(note["updated_time"])/1000.)
            logging.info("Comparing %s with %s" % (note_updated_time, options.updatedsince))

            if note_updated_time < options.updatedsince:
                logging.info("Reached old note (%s)" % note["id"])
                break

        with open(os.path.join(options.notesdir, filename), "r") as f:
            note_lines = f.readlines()

        note_title = note_lines.pop(0).strip()
        logging.debug("Extracted title: %s" % note_title)

        episode_num_match = re.search(episode_re, note_title)
        if episode_num_match:
            episode_num = episode_num_match.group(1)
            logging.debug("Extracted episode number: %s" % episode_num)
        else:
            episode_num = None
            logging.debug("No episode number found for title: %s" % note_title)

        meta_index = note_lines.index("id: %s\n" % note["id"])
        logging.debug("Found metadata starting on line %s" % meta_index)

        note_body = "".join(note_lines[:meta_index]).strip()

        image_srcs = re.findall(image_re, note_body)

        if image_srcs:
            for image_src in image_srcs:
                note_body = note_body.replace(":/%s" % image_src, "images/%s" % image_src)

        rendered_body = markdown2.markdown(note_body)

        result = template.replace("{{ TITLE }}", note_title)
        result = result.replace("{{ BODY }}", rendered_body)

        if episode_num:
            output_file = "Episode-%s.html" % str(episode_num).zfill(4);
        else:
            output_file = "%s.html" % note_title

        output_path = os.path.join(options.outputdir, output_file)
        logging.info("Writing rendered file to %s" % output_path)
        with open(output_path, "w") as f:
            f.write(result)

        if episode_num:
            episode_dir = str(episode_num).zfill(4);
            episode_dir_path = os.path.join(options.episodeguidedir, episode_dir)

            if not os.path.exists(episode_dir_path):
                os.makedirs(episode_dir_path)

            episode_guide_markdown_path = os.path.join(episode_dir_path, "agenda.md")

            logging.info("Writing episode guide markdown file to: %s" % episode_guide_markdown_path)
            with open(episode_guide_markdown_path, "w") as f:
                f.write(note_body)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Print debugging messages to the console.",
    )
    parser.add_argument(
        "--watch",
        action="store_true",
        help="Use watchman to watch the notesdir to trigger synchronization.",
        default=False,
    )
    parser.add_argument(
        "--config",
        type=str,
        dest="config",
        help="Configuration file",
        default="config.json",
    )
    parser.add_argument(
        "--template",
        type=str,
        dest="template",
        help="Template file",
        default="template.html.template",
    )
    parser.add_argument(
        "--notesdir",
        type=str,
        dest="notesdir",
        help="Markdown notes directory",
        required=True,
    )
    parser.add_argument(
        "--updatedsince",
        type=lambda s: datetime.datetime.strptime(s, '%Y-%m-%d %H:%M:%S'),
        dest="updatedsince",
        help="ISO date. Files changed after this date are considered changed.",
    )
    parser.add_argument(
        "--outputdir",
        type=str,
        dest="outputdir",
        help="Output directory",
        required=True,
    )
    parser.add_argument(
        "--episodeguidedir",
        type=str,
        dest="episodeguidedir",
        help="Episode guide _episodes directory",
        required=True,
    )

    options, extra = parser.parse_known_args(sys.argv[1:])

    if not options.watch and not options.updatedsince:
        parser.error("Must supply either --watch or --updatedsince")
        sys.exit(1)

    log_level = logging.DEBUG if options.verbose else logging.INFO
    logging.basicConfig(format="%(levelname)s:  %(message)s", level=log_level)

    if options.watch:
        watch(options)
    else:
        run(options)
