import csv

class ReadCSV:
    def __init__(self, filename, mode="reader"):
        self.filename = filename
        if mode == "dict_reader":
            self._csv_mode = csv.DictReader
        else:
            self._csv_mode = csv.reader
        self._mode_chose = {"reader": csv.reader, "dict_reader": csv.DictReader}
        self._csv_mode = self._mode_chose[mode]

    def read_from_csv(self):
        with open(self, 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=",")
            data = []
            for row in reader:
                data.append(row)
            return data

    #
    # def read_dict_from_csv(self):
    #     with open(self, 'r') as csv_file:
    #         reader = csv.DictReader(csv_file, delimiter=",")
    #         data = []
    #         for row in reader:
    #             data.append(row)
    #     return data

csv_reader = ReadCSV("111.csv")



