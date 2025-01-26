import os, fnmatch

def match(folder, search):
    for file_name in os.listdir(folder):
        if fnmatch.fnmatch(file_name, search):
            print(file_name, end='\n')

match('./PythonFundamentals', '*e.py')
match('./PythonFundamentals', '*r*.py')
match('./PythonFundamentals', '*ry')