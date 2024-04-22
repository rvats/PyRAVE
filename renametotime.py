import os
from datetime import datetime

# Function to rename JPG files based on creation time
def rename_files(folder_path):
    # List all files in the folder
    files = os.listdir(folder_path)
    
    # Filter JPG files
    jpg_files = [file for file in files if file.lower().endswith('.jpg')]
    
    # Sort JPG files by creation time
    jpg_files.sort(key=lambda x: os.path.getctime(os.path.join(folder_path, x)))
    
    # Rename JPG files with numbers based on creation time
    for i, jpg_file in enumerate(jpg_files):
        # Get creation time of the file
        creation_time = os.path.getctime(os.path.join(folder_path, jpg_file))
        # Convert creation time to a formatted string
        formatted_time = datetime.fromtimestamp(creation_time).strftime('%Y%m%d_%H%M%S')
        # Generate new file name with a number prefix
        new_name = f"{i+1:03d}_{formatted_time}.jpg"
        # Rename the file
        os.rename(os.path.join(folder_path, jpg_file), os.path.join(folder_path, new_name))
        print(f"Renamed {jpg_file} to {new_name}")

# Example usage
folder_path = "."  # Change this to the path of your folder
rename_files(folder_path)