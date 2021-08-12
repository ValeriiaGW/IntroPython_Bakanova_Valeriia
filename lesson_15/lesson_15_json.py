# наследование классов

import json

class JsonReader:
    def __init__(self, filename):
        self.filename = filename
        # self.data = None
        self.data = self.read_json()

    def read_json(self):
        with open(self.filename, "r") as json_file:
            # self.data = json.load(json_file)
            data = json.load(json_file)
            return data


class JsonWorkerList(JsonReader):

    def __init__(self, filename, limit):
        super().__init__(filename)
        self.data = self.data[:limit]

    def sort(self):
        self.data.sort()


class JsonWorkerDict(JsonReader):

    def sort(self):
        keys = sorted(self.data.keys())
        self.data = {key: self.data[key] for key in keys}


    def __repr__(self):
        return f"Dict filename: {super().__repr__()}"


json_worker_list = JsonWorkerList("data_list.json", 3)
json_worker_dict = JsonWorkerDict("data_dict.json")
print(json_worker_list.data)
print(json_worker_dict.data)
json_worker_list.sort()
json_worker_dict.sort()
print(json_worker_list.data)
print(json_worker_dict.data)