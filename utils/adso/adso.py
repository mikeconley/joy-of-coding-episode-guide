#!/usr/bin/env python

import argparse
import logging
import os
import progressbar
import sys


import scipy.io.wavfile as wav


from deepspeech.model import Model
from pyvtt import (WebVTTFile,
                   WebVTTItem,
                   WebVTTTime)


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

AUDIO_SEGMENT_SAMPLES = 16000 * 5 # 5 seconds


def sample_index_to_time(index):
    duration_seconds = index / 16000
    duration_minutes, duration_seconds = divmod(duration_seconds, 60)
    duration_hours, duration_minutes = divmod(duration_minutes, 60)
    return duration_hours, duration_minutes, duration_seconds


def main(options):
    logging.info("Will write VTT to %s" % options.output)
    # Make sure the WAV is to code...
    logging.info("Loading up WAV file at %s..." % options.wav)
    fs, audio = wav.read(options.wav)

    if fs != 16000:
        logging.error("Only 16000hz WAV files are usable.")
        sys.exit(1)

    total_samples = len(audio)
    duration_hours, duration_minutes, duration_seconds = sample_index_to_time(len(audio))
    logging.info("Approximate duration: %d:%02d:%02d" % (duration_hours, duration_minutes, duration_seconds))

    # Let's load up DeepSpeech and get it ready.
    logging.info("Loading pre-trained DeepSpeech model...")
    root_model_dir = os.path.join(options.deepspeech_model_dir, MODEL_DIR)

    model = os.path.join(root_model_dir, MODEL_FILE)
    alphabet = os.path.join(root_model_dir, MODEL_ALPHABET)
    lang_model = os.path.join(root_model_dir, MODEL_LANG_MODEL)
    trie = os.path.join(root_model_dir, MODEL_TRIE)

    deepspeech = Model(model, N_FEATURES, N_CONTEXT, alphabet, BEAM_WIDTH)
    logging.info("Done loading model.")

    logging.info("Loading language model...")
    deepspeech.enableDecoderWithLM(alphabet, lang_model, trie, LM_WEIGHT,
WORD_COUNT_WEIGHT, VALID_WORD_COUNT_WEIGHT)
    logging.info("Done loading model.")

    playhead = 0

    out = WebVTTFile()

    bar = progressbar.ProgressBar(max_value=total_samples)
    while playhead < (total_samples - 1):
        end_point = min(playhead + AUDIO_SEGMENT_SAMPLES, (total_samples - 1))
        segment = audio[playhead:end_point]
        inference = deepspeech.stt(segment, fs)
        logging.debug("Inferred: %s" % inference)

        start_hours, start_minutes, start_seconds = sample_index_to_time(playhead)
        playhead = end_point
        end_hours, end_minutes, end_seconds = sample_index_to_time(playhead)

        if not inference:
            continue

        start = WebVTTTime(start_hours, start_minutes, start_seconds)
        end = WebVTTTime(end_hours, end_minutes, end_seconds)

        item = WebVTTItem(0, start, end, inference)
        out.append(item)
        bar.update(playhead)

        out.save(options.output, encoding="utf-8")

    out.clean_indexes()
    out.save(options.output, encoding="utf-8")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--deepspeech-model-dir", type=str, required=True,
                        help="The folder where the Deepspeech pre-trained model is.")
    parser.add_argument("--wav", type=str, required=True,
                        help="16-bit 16000hz WAV to attempt to auto-transcribe.")
    parser.add_argument("--output", type=str, required=True,
                        help="Place to write the WebVTT output.")
    parser.add_argument("--verbose", action="store_true",
                        help="Print debugging messages to the console.")

    options, extra = parser.parse_known_args(sys.argv[1:])

    log_level = logging.DEBUG if options.verbose else logging.INFO
    logging.basicConfig(format="%(levelname)s:  %(message)s", level=log_level)

    sys.exit(main(options))
