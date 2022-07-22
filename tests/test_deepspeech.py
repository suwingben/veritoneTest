from verification.verify_wer import verify_transcription_accuracy
from client.deepContainer import deepspeechClient
import logging

import parametrize_from_file
import pytest


@parametrize_from_file
def test_deepspeech_transcription(audio_file, expected_phrase, test_container):

    actual_phrase = deepspeechClient(audio_file, test_container)

    accuracy_percent = verify_transcription_accuracy(actual_phrase, expected_phrase)

    return accuracy_percent
