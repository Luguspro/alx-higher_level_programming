#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list


print("\n")
my_list = [1, 2, 3, 4, 5]
idx = 3
element = 9
new_list = replace_in_list(my_list, idx, element)
print(new_list)
print(my_list)
