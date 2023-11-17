def count_lines(file_path):
    count = 0
    with open(file_path, 'r') as file:
        for line in file:
            count += 1
    return count

file_path = 'path/to/your/file.txt'
line_count = count_lines(file_path)
print(f"The number of lines in the file is: {line_count}")
