#Project Name: Desktop Cleaner
#Purpose: To automatically clean the downloads folder and sort the files into their respected folders.
#Author: Aidan Lui
#Date: Septembter 28 2025

import os 
import shutil
import hashlib
import logging
from pathlib import Path


#Variable Configuration
TARGET_FOLDER = Path.home() / "Downloads"
DUPLICATES_FOLDER = TARGET_FOLDER / "Duplicates"
LOG_FILE = TARGET_FOLDER / "cleanup-log.txt"

FILE_CATEGORIES = {
    "Documents": [".doc", ".docx", ".pdf", ".txt", ".xlsx", ".pptx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Videos": [".mp4", ".mvi", ".mov", ".mkv"],
    "Audio": [".mp3", ".wav", ".flac"],
    "Others": []
}

#Log file Setup
logging.basicConfig(filename = LOG_FILE,
                    level = logging.INFO,
                    format = '%(asctime)s - %(message)s')

#Helper Functions

#This function deals with hashing the files to detect duplicates. 
def get_file_hash(file_path):
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hasher.update(chunk)
        return hasher.hexdigest()

#This function deals with determing the catergory of the file and what folder they should be placed in.
def determine_category(file): 
    ext = file.suffix.lower()
    for category, extensions in FILE_CATEGORIES.items():
        if ext in extensions:
            return category
    return "Others"

#This function ensures that the folder exists but if it doesn't it creates it.
def move_file(file_path, dest_folder):
    dest_folder.mkdir(parents = True, exist_ok = True)
    shutil.move(str(file_path), str(dest_folder / file_path.name))
    logging.info(f"Moved {file_path} -> {dest_folder}")

#Main Function

#This function does the organizing and deals with duplicate folders based on the hashing.
def organize_folder():
    DUPLICATES_FOLDER.mkdir(exist_ok = True)
    seen_hashes = set()

    for file in TARGET_FOLDER.iterdir():
        if file.is_dir():
            continue
    
        file_hash = get_file_hash(file)
        if file_hash in seen_hashes:
            move_file(file, DUPLICATES_FOLDER)
            continue
        else:
            seen_hashes.add(file_hash)

        category = determine_category(file)
        dest_folder = TARGET_FOLDER / category
        move_file(file, dest_folder)

    print("Folder cleanup is complete.")

#Run Script
if __name__ == "__main__":
    organize_folder()
