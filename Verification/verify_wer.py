import jiwer





def verify_transcription_accuracy(percentage,expected_phrase,actual_phrase ):

    expected_phrase = "razu you must hurry you must stay the path "
    error_rate = jiwer.wer(actual_phrase, expected_phrase)

    assert error_rate > percentage

    return error_rate