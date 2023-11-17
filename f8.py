import os

def delete_file(path):
    if os.path.exists(path):
        if os.access(path, os.W_OK):
            os.remove(path)
            print(f"File {path} deleted successfully.")
        else:
            print(f"Permission denied: {path} is not writable.")
    else:
        print(f"File {path} does not exist.")

delete_file("/path/to/file.txt")
