# Adso

Adso is a utility script that currently takes 16-bit 16000hz WAV files from Joy of Coding videos, and attempts to transcribe them to [the WebVTT format](https://developer.mozilla.org/en-US/docs/Web/API/WebVTT_API) using [Mozilla Deepspeech](https://github.com/mozilla/DeepSpeech).

Adso is named after the character Adso of Melk from Umberto Eco's [The Name of the Rose](https://en.wikipedia.org/wiki/The_Name_of_the_Rose).

## Usage

You must ensure that the WAV file has a sample rate of 16000hz (you can use [Audacity](https://www.audacityteam.org/) to convert if needs be) and is 16-bit.

I recommend creating a [virtualenv](https://virtualenv.pypa.io/en/stable/) while working with Adso.

Once inside your virtual environment, install the dependencies:

    pip install -r requirements.txt

And then [download the pre-trained speech and language models for Mozilla Deepspeech](https://github.com/mozilla/DeepSpeech/releases). This should be the `deepspeech-x.x.x-models.tar.gz` file. Decompress that file somewhere, and then you can use Adso like so:

    python adso.py --wav <path-to-wave> --deepspeech-model-dir <path-to-deepspeech-model> --output <name-of-VTT-output>

Example:

    python adso.py --wav JoC129.wav --deepspeech-model-dir ~/Projects/deepspeech-model --output JoC129.vtt

Then sit back and wait. The transcription might take a few hours depending on the speed of your machine.
