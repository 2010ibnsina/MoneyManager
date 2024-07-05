import pytest
from tkinter import Tk
from Feedback import Feedback


@pytest.fixture
def feedback_instance():
    root = Tk()
    feedback = Feedback(root)
    return feedback


@pytest.fixture
def mock_feedback_window():
    return Tk()

def test_submit_data_valid(mock_feedback_window):
    feedback = Feedback(mock_feedback_window)
    feedback.submit_data("Mar 08 2024", "test income", "500")
    assert feedback.warning_label.cget("text") == "Successfully Submitted!!"

def test_submit_data_no_source(mock_feedback_window):
    feedback = Feedback(mock_feedback_window)
    feedback.submit_data("Mar 08 2023", "", "5000")
    assert feedback.warning_label.cget("text") == "Please Enter Income Source"

def test_submit_data_no_amount(mock_feedback_window):
    feedback = Feedback(mock_feedback_window)
    feedback.submit_data("Mar 08 2023", "Salary", "")
    assert feedback.warning_label.cget("text") == "Please Enter Income Amount"

def test_submit_data_no_data(mock_feedback_window):
    feedback = Feedback(mock_feedback_window)
    feedback.submit_data("Mar 08 2023", "", "")
    assert feedback.warning_label.cget("text") == "Please provide data in both field."

def test_submit_data_invalid_amount(mock_feedback_window):
    feedback = Feedback(mock_feedback_window)
    feedback.submit_data("Mar 08 2023", "Salary", "abc")
    assert feedback.warning_label.cget("text") == "Income Amount Can Be Only Positive Numbers"
