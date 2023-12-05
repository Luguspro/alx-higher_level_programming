#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list.copy()
    new_list = my_list.copy()
    new_list[idx] = element
    return new_list

print("\n")
my_list = [1, 2, 3, 4, 5]
idx = 3
element = 9
new_list = new_in_list(my_list, idx, element)
print(new_list)
print(my_list)
