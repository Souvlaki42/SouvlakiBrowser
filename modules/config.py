from genericpath import exists
import json, sys

class JsonParser():
    def __init__(self, file):
        if not exists(file):
            sys.exit("This file doesn't exist!")
        self.file = file

    def read_key(self, keypath, seperator = "/"):
        keys = keypath.split(seperator)
        with open(self.file) as file:
            key0 = keys[0]
            data = json.load(file)[key0]
            del keys[0]
            for key in keys:
                data = data[key]
            return data

    def write_key(self, keypath, value, seperator = "/", intents = 4):
        keys = keypath.split(seperator)
        with open(self.file) as file:
            data = json.load(file)
            data2 = data
            lastKey = keys.pop()
        with open(self.file, "w") as file:
            for key in keys:
                data2 = data2[key]
            data2[lastKey] = value
            json.dump(data, file, indent = intents)

jsonParser = JsonParser("config.json")