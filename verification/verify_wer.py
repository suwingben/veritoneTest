import jiwer
import logging

console_logger = logging.getLogger("console")


def verify_transcription_accuracy(expected_phrase, actual_phrase):
    minimum_percentage = 0.8
    test_logger = logging.getLogger("test_data_log")

    # Jiwer was pretty easy to implement and got the goodies pretty fast.
    # could have used some other formatting stuff to strip punctuation just in case.
    error_rate = 1 - jiwer.wer(actual_phrase, expected_phrase)

    #Percentage to make it actually readable by a human.
    percentage = error_rate * 100

    #Logging the long phrases over to the console for easy viewing and the test logger bumping things off to the log in a way that we can split on a character.
    console_logger.info(f"The expected_phase is : {expected_phrase}")
    console_logger.info(f"The transcribed phase is : {actual_phrase}")
    console_logger.info(f"The accuracy percentage is : {percentage}")
    test_logger.info(f"Accuracy:{percentage}")
    test_logger.info(f"Transcription from DeepSpeech: {actual_phrase}")

    # Here I try to snag the assertion failing for the pass fail. Surprisingly, if you catch but don't throw the AssertionError things show up as passing, which is why I had to raise e at the end.
    try:
        assert error_rate > minimum_percentage
        console_logger.info(
            f"Test passed with an accuracy percentage of {percentage} which is above the threshold of {minimum_percentage * 100}")
        test_logger.info(
            f"Test passed with an accuracy percentage of {percentage} which is above the threshold of {minimum_percentage * 100}")
    #On a failure, log the failure and the reason why. Throw the error so that we fail the test still.
    except AssertionError as e:
        console_logger.info(
            f"Test failed with accuracy of {percentage}% which is below the threshold of {minimum_percentage * 100}%")
        test_logger.info(
            f"Test failed with an accuracy of {percentage} %which is below the threshold of {minimum_percentage * 100}%")
        raise e
    return error_rate
