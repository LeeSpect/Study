# Key 기준으로 정렬 (오름차순)

# 다음과 같이 sorted()를 이용하여 dict를 정렬할 수 있습니다. 
# 인자로 my_dict.items()를 전달하면 오름차순으로 정렬됩니다.
my_dict = {'c': 3, 'a': 1, 'b': 2, 'e': 1, 'd': 2}

sorted_dict = sorted(my_dict.items())
print(sorted_dict)

# sorted()는 다음과 같이 Tuple pair로 이루어진 List를 리턴합니다.
[('a', 1), ('b', 2), ('c', 3), ('d', 2), ('e', 1)]

# 참고로, my_dict.items()를 출력해보면 다음과 같이 Tuple pair로 이루어진 List가 리턴됩니다.
print(my_dict.items())
# Output:
dict_items([('c', 3), ('a', 1), ('b', 2), ('e', 1), ('d', 2)])


# Key를 기준으로 정렬(내림차순)

# 내림차순으로 정렬하려면 sorted()에 다음과 같이 reverse = True를 인자로 전달해야 합니다.
# 여기서 lambda가 인자로 전달되는데 item[0]는 dict의 key를 의미합니다.
sorted_dict = sorted(my_dict.items(), key = lambda item: item[0], reverse = True)
print(sorted_dict)
# Output:
[('e', 1), ('d', 2), ('c', 3), ('b', 2), ('a', 1)]


# Value를 기준으로 정렬 (오름차순)

# 다음과 같이 sorted()를 사용하여 Value를 기준으로 정렬할 수 있습니다.
# 인자로 lambda가 전달되는데 item[1]은 dict의 Value를 의미합니다.
sorted_dict = sorted(my_dict.items(), key = lambda item: item[1])
print(sorted_dict)
# Output:
[('a', 1), ('e', 1), ('b', 2), ('d', 2), ('c', 3)]


# Value를 기준으로 정렬 (내림차순)

# 내림차순으로 정렬하려면 다음과 같이 sorted()에 인자로 reverse = True를 전달하면 됩니다.
sorted_dict = sorted(my_dict.items(), key = lambda item: item[1], reverse = True)
print(sorted_dict)
# Output:
[('c', 3), ('b', 2), ('d', 2), ('a', 1), ('e', 1)]


# 출처 : https://codechacha.com/ko/python-sorting-dict/
