import jiwer
import logging

console_log = logging.getLogger('console')
test_log = logging.getLogger('test_logger')


def verify_transcription_accuracy(expected_phrase,actual_phrase):

    minimum_percentage = 0.8


    error_rate = 1 - jiwer.wer(actual_phrase, expected_phrase)


    console_log.debug(f'The expected_phase is :{expected_phrase}')
    console_log.debug(f'The transcribed phase is : {actual_phrase}')
    console_log.debug(f'The accuracy is: {error_rate}')
    test_log = logging.getLogger('test_logger')
    test_log.debug(f'The accuracy is: {error_rate}')

    assert error_rate > minimum_percentage

    return error_rate