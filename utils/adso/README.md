# Adso

Adso is a utility script that currently takes 16-bit 16000hz WAV files from Joy of Coding videos, and attempts to transcribe them to [the WebVTT format](https://developer.mozilla.org/en-US/docs/Web/API/WebVTT_API) using [Mozilla DeepSpeech](https://github.com/mozilla/DeepSpeech).

Adso is named after the character Adso of Melk from Umberto Eco's [The Name of the Rose](https://en.wikipedia.org/wiki/The_Name_of_the_Rose).

## Usage

A recent version of [ffmpeg](https://www.ffmpeg.org/) must be available on the system for Adso to work properly.

I also recommend creating a [virtualenv](https://virtualenv.pypa.io/en/stable/) while working with Adso.

Once inside your virtual environment, install the dependencies:

    pip install -r requirements.txt

And then [download the pre-trained speech and language models for Mozilla DeepSpeech](https://github.com/mozilla/DeepSpeech/releases). This should be the `deepspeech-x.x.x-models.tar.gz` file. Decompress that file somewhere, and then you can use Adso like so:

    python adso.py --vid-url <URL-to-video> --deepspeech-model-dir <path-to-deepspeech-model> --output <name-of-VTT-output>

Example:

    python adso.py --vid-url "https://vid.ly/i6y5i9?content=video&format=webm" --deepspeech-model-dir ~/Projects/deepspeech-model --output JoC129.vtt

Then sit back and wait a while. The transcription might take a few hours depending on the speed of your machine.
