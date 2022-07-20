from Verification.verify_wer import verify_transcription_accuracy
from Client.deepContainer import deepspeechClient
import pytest
import logging






def test_deepspeech_transcription():
    #use conftest to read file
    #File contains : percentage threshhold, test data pairs (unless i figure out how to extract)


    #call the container with test data
    actual_phrase = deepspeechClient(test_container,audio_file)

    accuracy_percent = verify_transcription_accuracy(actual_phrase,expected_phrase)

    