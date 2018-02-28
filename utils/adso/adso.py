#!/usr/bin/env python

from argparse import ArgumentParser
from deepspeech.model import Model
from os import close, path
from progressbar import ProgressBar
from pyvtt import (WebVTTFile, WebVTTItem, WebVTTTime)
from re import sub
from requests import get
from subprocess import call
from sys import argv, exit
from tempfile import NamedTemporaryFile, mkstemp
from textwrap import fill
import logging as log
import scipy.io.wavfile as wav

MODEL_DIR = "models"
MODEL_FILE = "output_graph.pb"
MODEL_ALPHABET = "alphabet.txt"
MODEL_LANG_MODEL = "lm.binary"
MODEL_TRIE = "trie"

# Number of MFCC features to use
N_FEATURES = 26
# Size of the context window used for producing timesteps in the input vector
N_CONTEXT = 9
# Beam width used in the CTC decoder when building candidate transcriptions
BEAM_WIDTH = 500
# The alpha hyperparameter of the CTC decoder. Language Model weight
LM_WEIGHT = 1.75
# The beta hyperparameter of the CTC decoder. Word insertion weight (penalty)
WORD_COUNT_WEIGHT = 1.00
# Valid word insertion weight. This is used to lessen the word insertion penalty
# when the inserted word is part of the vocabulary
VALID_WORD_COUNT_WEIGHT = 1.00

AUDIO_SEGMENT_SAMPLES = 16000 * 5  # 5 seconds

DOWNLOAD_CHUNK_SIZE = 4096  # bytes

MAX_CAPTION_WIDTH = 40

INFERENCE_REPLACEMENTS = {
    "cant": "can't",
    "dont": "don't",
    "i": "I",
    "im": "I'm",
    "joy of coding": "Joy of Coding",
    "mike": "Mike",
}


def sample_index_to_time(index):
    duration_seconds = index / 16000
    duration_minutes, duration_seconds = divmod(duration_seconds, 60)
    duration_hours, duration_minutes = divmod(duration_minutes, 60)
    return duration_hours, duration_minutes, duration_seconds


def run_ffmpeg(args):
    try:
        all_args = ["ffmpeg"] + args
        print "Running: %s" % (' '.join(all_args))
        call(["ffmpeg"] + args)
        return True
    except OSError as e:
        return False


def main(options):
    # Ensure ffmpeg is around
    if not run_ffmpeg(['-version']):
        log.error(
            "ffmpeg needs to be available to strip audio from the video file.")
        exit(1)

    with NamedTemporaryFile(delete=True) as vid_file:
        log.info("Downloading %s - this might take a while." % options.vid_url)
        response = get(options.vid_url, stream=True)
        total_length = response.headers.get("content-length")
        if total_length is None:  # no content length header
            log.info("Unknown length - can't predict how long this will take.")
            f.write(response.content)
        else:
            bar = ProgressBar(max_value=int(total_length))
            dl = 0
            for data in response.iter_content(chunk_size=DOWNLOAD_CHUNK_SIZE):
                dl += len(data)
                vid_file.write(data)
                vid_file.flush()
                bar.update(dl)

        log.info("Download done. Stripping audio.")
        (wav_file, wav_file_name) = mkstemp('.wav')
        result = run_ffmpeg([
            "-y", "-i", vid_file.name, "-vn", "-acodec", "pcm_s16le", "-ar",
            "16000", "-ac", "1", wav_file_name
        ])
        if not result:
            close(wav_file)
            log.error("ffmpeg failed. Bailing.")
            exit(1)

        fs, audio = wav.read(wav_file_name)
        close(wav_file)

    log.info("Will write VTT to %s" % options.output)
    # Make sure the WAV is to code...
    log.info("Loading up WAV file...")

    if fs != 16000:
        log.error("Only 16000hz WAV files are usable.")
        exit(1)

    total_samples = len(audio)
    duration_hours, duration_minutes, duration_seconds = sample_index_to_time(
        len(audio))
    log.info("Approximate duration: %d:%02d:%02d" %
             (duration_hours, duration_minutes, duration_seconds))

    # Let's load up DeepSpeech and get it ready.
    log.info("Loading pre-trained DeepSpeech model...")
    root_model_dir = path.join(options.deepspeech_model_dir, MODEL_DIR)

    model = path.join(root_model_dir, MODEL_FILE)
    alphabet = path.join(root_model_dir, MODEL_ALPHABET)
    lang_model = path.join(root_model_dir, MODEL_LANG_MODEL)
    trie = path.join(root_model_dir, MODEL_TRIE)

    deepspeech = Model(model, N_FEATURES, N_CONTEXT, alphabet, BEAM_WIDTH)
    log.info("Done loading model.")

    log.info("Loading language model...")
    deepspeech.enableDecoderWithLM(alphabet, lang_model, trie, LM_WEIGHT,
                                   WORD_COUNT_WEIGHT, VALID_WORD_COUNT_WEIGHT)
    log.info("Done loading model.")

    playhead = 0

    out = WebVTTFile()

    bar = ProgressBar(max_value=total_samples)
    while playhead < (total_samples - 1):
        end_point = min(playhead + AUDIO_SEGMENT_SAMPLES, (total_samples - 1))
        segment = audio[playhead:end_point]
        inference = deepspeech.stt(segment, fs)
        log.debug("Inferred: %s" % inference)

        start_hours, start_minutes, start_seconds = sample_index_to_time(
            playhead)
        playhead = end_point
        end_hours, end_minutes, end_seconds = sample_index_to_time(playhead)

        if not inference:
            continue

        for search, replace in INFERENCE_REPLACEMENTS.iteritems():
            inference = sub(r"\b" + search + r"\b", replace, inference)

        inference = fill(inference, width=MAX_CAPTION_WIDTH)

        start = WebVTTTime(start_hours, start_minutes, start_seconds)
        end = WebVTTTime(end_hours, end_minutes, end_seconds)

        item = WebVTTItem(0, start, end, inference)
        out.append(item)
        bar.update(playhead)

        out.save(options.output, encoding="utf-8")

    out.clean_indexes()
    out.save(options.output, encoding="utf-8")


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        "--deepspeech-model-dir",
        type=str,
        required=True,
        help="The folder where the Deepspeech pre-trained model is.")
    parser.add_argument(
        "--vid-url",
        type=str,
        required=True,
        help="URL of video to download, strip audio and transcribe.")
    parser.add_argument(
        "--output",
        type=str,
        required=True,
        help="Place to write the WebVTT output.")
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Print debugging messages to the console.")

    options, extra = parser.parse_known_args(argv[1:])

    log_level = log.DEBUG if options.verbose else log.INFO
    log.basicConfig(format="%(levelname)s:  %(message)s", level=log_level)

    exit(main(options))
