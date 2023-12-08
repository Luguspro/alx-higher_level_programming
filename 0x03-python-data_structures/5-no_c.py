#!/usr/bin/python3
def no_c(my_string):
    char = ""
    for i in my_string:
        if i.lower() != 'c' or i.upper() != 'C':
            char += i
    return char


print("\n")
print(no_c("Best School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))
