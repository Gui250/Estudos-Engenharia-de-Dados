import os 
from .AbstractDataSource import AbstractDataSource

class FileSource(AbstractDataSource):
    def __init__(self):
        self.previous_file = []
        self.start()

    
    def create_path(self): 
        current_directory = os.getcwd()
        self.folder_path = os.path.join(current_directory, 'data', 'extension_files')
        if not os.path.exists(self.folder_path): 
            os.makedirs(self.folder_path)