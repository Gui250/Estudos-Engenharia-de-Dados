import os 
import pandas as pd 
from .FilesSource import FileSource


class CsvSource(FileSource):
    def create_path(self):
        base_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.folder_path = os.path.join(base_directory, 'data', 'csv_files')
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)
    
    def check_for_new_files(self):
        current_files = os.listdir(self.folder_path)
        new_files = [file for file in current_files if file not in self.previous_file and file.endswith(".csv")]

        if new_files:
            print("New files detected: ", new_files)
            self.previous_file = current_files
            self.get_data()
        else:
            print("No new CSV files detected")

    def get_data(self):
        data_frames = []
        for file_path in self.previous_file:
            try:
                path = f'{self.folder_path}/{file_path}'
                data = pd.read_csv(path)
                data_frames.append(data)
            except Exception as e: 
                print("Um erro foi achado ao ler arquivo csv", e)

        if data_frames:
            self.combined_data = pd.concat(data_frames, ignore_index=True)
            print(self.combined_data)
            return self.combined_data