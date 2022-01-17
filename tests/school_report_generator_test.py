from src.school_report_generator import report_generator

def test_when_given_a_Green_score_return_Green_1():
    assert report_generator("Green") == "Green: 1"