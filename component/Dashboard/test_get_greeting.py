from datetime import datetime
from unittest.mock import patch
from header import Header 


class TestHeader:
    @patch('header.datetime')
    def test_good_morning(self, mock_datetime):
        mock_datetime.now.return_value.hour = 8 
        header = Header(None)  
        assert header.get_greeting() == "Good Morning"

    @patch('header.datetime')
    def test_good_noon(self, mock_datetime):
        mock_datetime.now.return_value.hour = 12 
        header = Header(None)
        assert header.get_greeting() == "Good Afternoon"

    @patch('header.datetime')
    def test_good_afternoon(self, mock_datetime):
        mock_datetime.now.return_value.hour = 15 
        header = Header(None)
        assert header.get_greeting() == "Good Afternoon"

    @patch('header.datetime')
    def test_good_night(self, mock_datetime):
        mock_datetime.now.return_value.hour = 21  
        header = Header(None)
        assert header.get_greeting() == "Good Evening"
