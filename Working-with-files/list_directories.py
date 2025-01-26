# Listing files from perticular folder
import os

def list_dir(folder):
    for file_name in os.listdir(folder):
        print(file_name, end='\n')

list_dir('./Classes')