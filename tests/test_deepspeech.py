from Verification.verify_wer import verify_transcription_accuracy
from Client.deepContainer import deepspeechClient
import pytest

import json
import parametrize_from_file
import pytest


@parametrize_from_file
def test_deepspeech_transcription(audio_file, expected_phrase, test_container):
    # use conftest to read file
    # File contains : percentage threshhold, test data pairs (unless i figure out how to extract)


    # call the container with test data
    actual_phrase = deepspeechClient(audio_file, test_container)



    accuracy_percent = verify_transcription_accuracy(actual_phrase, expected_phrase)

    print(accuracy_percent)
