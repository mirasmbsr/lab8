def all_true(elements):
    return all(elements)


my_tuple = (True, True, True, False)
result = all_true(my_tuple)

print(result)