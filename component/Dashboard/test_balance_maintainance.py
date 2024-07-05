import pytest
from show_info import ShowInfo

@pytest.fixture
def show_info_instance():
    return ShowInfo(window=None)

def test_total_balance_calculation(show_info_instance):
    show_info_instance.data.calculate_income_expenses = lambda: ({'income1': 100, 'income2': 200}, {'expense1': 50, 'expense2': 75})
    
    show_info_instance.update_balance_labels()

    assert show_info_instance.total_balance == 175  # (100 + 200) - (50 + 75) = 275 - 125 = 175
