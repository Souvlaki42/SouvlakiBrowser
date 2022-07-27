import json

class JsonWorker():
    def __init__(self, file) -> None:
        super(self, file).__init__()
        self.file = file

    def read_file(self):
        with open(self.file, "r") as file:
            return json.load(file)

    def write_file(self, data):
        with open(self.file, "w") as file:
            return json.dump(data, file)

    def read_key(self, key):
        with open(self.file, "r") as file:
            return json.load(file)[key]

    def write_key(self, key, value):
        with open(self.file, "r+") as file:
            data = json.load(file)
            data[key] = value
            file.seek(0)
            json.dump(data, file, indent = 1)
            file.truncate()