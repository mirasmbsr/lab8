
import os

def list_directories_files(path):
    directories = []
    files = []
    all_directories_files = []

    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            directories.append(item)
        elif os.path.isfile(item_path):
            files.append(item)

    all_directories_files = directories + files

    return directories, files, all_directories_files

# Example usage:
path = "/path/to/directory"
directories, files, all_directories_files = list_directories_files(path)

print("Directories:")
for directory in directories:
    print(directory)

print("Files:")
for file in files:
    print(file)

print("All Directories and Files:")
for item in all_directories_files:
    print(item)
