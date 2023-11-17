my_list = [input() for _ in range(int(input()))]
file_path = 'output.txt'

with open(file_path, 'w') as f:
    f.write('\n'.join(map(str, my_list)))