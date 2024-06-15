import json
import os

class FileHandler:
    def __init__(self, db_name):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.file_path = os.path.join(base_dir, '..', 'db', db_name)


    def read(self):
        with open(self.file_path, 'r') as file:
            if os.stat(self.file_path).st_size == 0:
                return []
            data = json.load(file)
        return data

    def write(self, data):
        with open(self.file_path, 'w') as file:
            json.dump(data, file, indent=4)