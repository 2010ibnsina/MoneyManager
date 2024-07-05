import csv


class DataHandler:
    def __init__(self, filename):
        self.filename = filename

    def data_write(self, field):
        with open(self.filename, 'a', newline="") as file:
            csv.writer(file).writerow(field)
            file.close()

