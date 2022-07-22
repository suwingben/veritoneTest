import jiwer
import logging

console_logger = logging.getLogger("console")


def verify_transcription_accuracy(expected_phrase, actual_phrase):

    minimum_percentage = 0.8
    test_logger = logging.getLogger("test_data_log")

    error_rate = 1 - jiwer.wer(actual_phrase, expected_phrase)

    percentage = error_rate * 100
    logging.info(f"The expected_phase is : {expected_phrase}")
    logging.info(f"The transcribed phase is : {actual_phrase}")
    logging.info(f"The accuracy percentage is : {percentage}")
    test_logger.info(f"Accuracy:{percentage}")
    test_logger.info(f"Transcription from DeepSpeech: {actual_phrase}")


    assert error_rate > minimum_percentage , f"Test failed with an error rate of {error_rate} which is below the threshold of {minimum_percentage}"

    return error_rate
