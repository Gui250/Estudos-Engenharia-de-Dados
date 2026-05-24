import os 
from .AbstractDataSource import AbstractDataSource

class FileSource(AbstractDataSource):
    def __init__(self):
        self.previous_file = []
        self.start()

    def start(self):
        self.create_path()

    def transform_data_to_df(self):
        return self.get_data()

    def create_path(self):
        base_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.folder_path = os.path.join(base_directory, 'data', 'extension_files')
        if not os.path.exists(self.folder_path): 
            os.makedirs(self.folder_path)

    def check_for_new_files(self):
        current_files = os.listdir(self.folder_path)
        new_files = [file for file in current_files if file not in self.previous_file]

        if new_files:
            print("New Files detected: ", new_files)
            self.previous_file = current_files
        else:
            print("No new files detected")