import csv
from datetime import datetime
from pathlib import Path

import pytest
from DataManager import DataManager  
data_path = Path(__file__).parent.parent.parent / "data_store" / "data.csv"

@pytest.fixture
def sample_instance():
    instance = DataManager(data_path)
    return instance

def test_data_sorted_by_date(sample_instance):
    data = sample_instance.get_data()
    dates = [datetime.strptime(row[1], "%b %d %Y") for row in data[1:]]
    assert dates == sorted(dates)

def test_summary_by_date(sample_instance):
    data = sample_instance.get_data()
    summary = {}
    for row in data[1:]:
        date_string = row[1]
        source = row[2]
        amount = float(row[3])
        date = datetime.strptime(date_string, "%b %d %Y").date()
        if date not in summary:
            summary[date] = {}
        if source not in summary[date]:
            summary[date][source] = 0
        summary[date][source] += amount
    
    assert summary[datetime.strptime(date_string, "%b %d %Y").date()] == {'zzz': 1000 }


