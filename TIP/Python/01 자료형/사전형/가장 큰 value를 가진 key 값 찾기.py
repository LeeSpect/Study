my_dict = {'a': 10, 'b': 5, 'c': 20}

max_key = max(my_dict, key=lambda k: my_dict[k])

print(max_key, my_dict[max_key]) # Output: c 20
