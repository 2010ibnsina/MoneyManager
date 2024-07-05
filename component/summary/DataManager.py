import csv
from datetime import datetime

class DataManager:
    def __init__(self, data_filename):
        self.data_filename = data_filename

    def get_data(self):
        with open(self.data_filename, "r", newline="") as file:
            reader = csv.reader(file)
            data = list(reader)
            header = data[0]
            d_sorted = sorted(data[1:], key=self.extract_date)
            d_sorted.insert(0, header)
            return d_sorted

    @staticmethod
    def extract_date(row):
        date_string = row[1]
        try:
            return datetime.strptime(date_string, "%b %d %Y")
        except ValueError:
            try:
                return datetime.strptime(date_string, "%b %d %y")
            except ValueError:
                return datetime.now()
