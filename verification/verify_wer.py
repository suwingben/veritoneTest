import jiwer
import logging

console_logger = logging.getLogger("console")


def verify_transcription_accuracy(expected_phrase, actual_phrase):

    minimum_percentage = 0.8
    test_logger = logging.getLogger("test_data_log")

    error_rate = 1 - jiwer.wer(actual_phrase, expected_phrase)

    percentage = error_rate * 100
    console_logger.info(f"The expected_phase is : {expected_phrase}")
    console_logger.info(f"The transcribed phase is : {actual_phrase}")
    console_logger.info(f"The accuracy percentage is : {percentage}")
    test_logger.info(f"Accuracy:{percentage}")
    test_logger.info(f"Transcription from DeepSpeech: {actual_phrase}")

    try:
        assert error_rate > minimum_percentage
        console_logger.info(f"Test passed with an accuracy percentage of {percentage} which is above the threshold of {minimum_percentage * 100}")
        test_logger.info(f"Test passed with an accuracy percentage of {percentage} which is above the threshold of {minimum_percentage * 100 }")

    except AssertionError as e:
        console_logger.info(f"Test failed with accuracy of {percentage}% which is below the threshold of {minimum_percentage * 100 }%")
        test_logger.info(f"Test failed with an accuracy of {percentage}%which is below the threshold of {minimum_percentage * 100}%")
        raise e
    return error_rate
