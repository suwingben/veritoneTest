import jiwer





def verify_transcription_accuracy(expected_phrase,actual_phrase ):

    minimum_percentage = 0.8

    error_rate = 1 - jiwer.wer(actual_phrase, expected_phrase)



    assert error_rate > minimum_percentage

    return error_rate