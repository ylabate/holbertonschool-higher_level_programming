#!/usr/bin/python3
def no_c(my_string):
    my_string_copy = ""
    for i in my_string:
        if i != 'C' and i != 'c':
            my_string_copy = my_string_copy + i
    return (my_string_copy)


if __name__ == "__main__":
    print(no_c("best school"))
