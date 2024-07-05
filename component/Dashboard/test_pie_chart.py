import pytest
from body import Body

class MockFileHandling:
    def calculate_income_expenses(self):
        return {'Salary': 5000, 'Investment': 2000}, {'Rent': 1000, 'Groceries': 500}

@pytest.fixture
def body():
    body = Body(None)
    body.file_handler = MockFileHandling()
    return body

def test_draw_pie_charts(body):
    body.draw_pie_charts()
    assert len(body.canvas.find_all()) > 0
