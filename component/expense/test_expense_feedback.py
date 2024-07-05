import pytest
from tkinter import Tk
from FeedBack import Feedback 


@pytest.fixture
def feedback_instance():
    root = Tk()
    feedback = Feedback(root)
    return feedback


import pytest
from tkinter import Tk 
from FeedBack import Feedback  

@pytest.fixture
def mock_feedback_window():
    return Tk()

def test_submit_data_valid(mock_feedback_window):
    feedback = Feedback(mock_feedback_window)
    feedback.submit_data("Mar 08 2023", "test cost", "100")
    assert feedback.warning_label.cget("text") == "Successfully Submitted!!"

def test_submit_data_no_source(mock_feedback_window):
    feedback = Feedback(mock_feedback_window)
    feedback.submit_data("Mar 08 2023", "", "100")
    assert feedback.warning_label.cget("text") == "Please Enter Expense Reason"

def test_submit_data_no_amount(mock_feedback_window):
    feedback = Feedback(mock_feedback_window)
    feedback.submit_data("Mar 08 2023", "test cost", "")
    assert feedback.warning_label.cget("text") == "Please Enter Expense Amount"

def test_submit_data_no_data(mock_feedback_window):
    feedback = Feedback(mock_feedback_window)
    feedback.submit_data("Mar 08 2023", "", "")
    assert feedback.warning_label.cget("text") == "Please provide data in both field."

def test_submit_data_invalid_amount(mock_feedback_window):
    feedback = Feedback(mock_feedback_window)
    feedback.submit_data("Mar 08 2023", "test cost", "abc")
    assert feedback.warning_label.cget("text") == "Expense Amount Can Be Only Positive Numbers"
