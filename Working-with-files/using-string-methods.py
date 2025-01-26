import os
from dataclasses import dataclass

@dataclass
class Files:
    folder: str
    search: str

    def ends_with(self):
        for file_name in os.listdir(self.folder):
            if file_name.endswith(self.search):
                print(file_name)
            else: 
                print('no file')
    
    def starts_with(self):
        for file_name in os.listdir(self.folder):
            if file_name.startswith(self.search):
                print(file_name)
            else:
                print('no file')
            
file = Files('./Classes', '.py')
file.ends_with()