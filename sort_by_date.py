import os, sys
import shutil
from datetime import datetime

def sort_by_date(folder_path):
    files = os.listdir(folder_path)
    for file_name in files:
        file_path = os.path.join(folder_path, file_name)
        file_date = datetime.fromtimestamp(os.path.getmtime(file_path))
        
        folder_path_by_date = os.path.join(folder_path,
                            f"{file_date.year}-{file_date.month:02d}")
        
        if not os.path.exists(folder_path_by_date):
            os.makedirs(folder_path_by_date)

        new_file_path = os.path.join(folder_path_by_date, file_name)
        shutil.move(file_path, new_file_path)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <folder_path>")
        sys.exit(1)

    target_folder = sys.argv[1]

    if not os.path.exists(target_folder):
        print("Error: File not found")
        sys.exit(1)

    sort_by_date(target_folder)