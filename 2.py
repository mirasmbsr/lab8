
def count_letters(string):
    upper_count = 0
    lower_count = 0
    
    for char in string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    
    return upper_count, lower_count


input_string = input()
upper, lower = count_letters(input_string)
print(upper)
print(lower)
