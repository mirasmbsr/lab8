import os

def test_path(path):
    if os.path.exists(path):
        print(f"{path} exists")
        filename = os.path.basename(path)
        directory = os.path.dirname(path)
        print(f"Filename: {filename}")
        print(f"Directory: {directory}")
    else:
        print(f"{path} does not exist")
