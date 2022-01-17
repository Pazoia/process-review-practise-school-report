from src.school_report_generator import report_generator

def test_when_given_a_Green_score_return_Green_1():
    assert report_generator("Green") == "Green: 1"

def test_when_given_a_Amber_score_return_Amber_1():
    assert report_generator("Amber") == "Amber: 1"

def test_when_given_a_Red_score_return_Red_1():
    assert report_generator("Red") == "Red: 1"
    