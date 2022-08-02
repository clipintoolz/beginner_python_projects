#!/usr/bin/env python3.10

# scans for the folder with the most files
import os
from pathlib import Path

number_of_files_in_folder = 0
folder_with_highest_number_of_files = ""

for dirpath, dirnames, filenames in os.walk(Path.home()):
    
    if len(filenames) > number_of_files_in_folder:
        
        number_of_files_in_folder = len(filenames)
        folder_with_highest_number_of_files = dirpath
        
print(f"{folder_with_highest_number_of_files} has the most files with about {number_of_files_in_folder} files")

