import string
def generate_files():
    for letter in string.ascii_uppercase:
        file_name = f"{letter}.txt"
        with open(file_name, 'w') as file:
            file.write(f"This is the content of {file_name}")

if __name__ == "__main__":
    generate_files()
