from utils.file_handler import FileHandler

class BaseService:
    def __init__(self, file_path):
        self.file_handler = FileHandler(file_path)

    def load_data(self, class_name):
        data = self.file_handler.read()
        return [class_name(**each) for each in data]