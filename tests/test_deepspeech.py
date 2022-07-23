from verification.verify_wer import verify_transcription_accuracy
from client.deepContainer import deepspeechClient
import logging

import parametrize_from_file
import pytest

#This fixture(?) calls the XML file that's named the same way as the test.
#The parameters in the XML need to be the same number and order as the parameters to pass to the test function
@parametrize_from_file
def test_deepspeech_transcription(audio_file, expected_phrase, test_container):

    #Just snag some output from the test container
    #Passing in test container in case we want to do testing across different versions
    #For example this test is against :latest but we could go against :2.2 or whatever
    actual_phrase = deepspeechClient(audio_file, test_container)

    #This jumps over to the verification to get the WER
    accuracy_percent = verify_transcription_accuracy(actual_phrase, expected_phrase)

    return accuracy_percent
