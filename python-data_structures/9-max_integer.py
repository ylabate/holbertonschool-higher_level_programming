#!/usr/bin/python3
def max_integer(my_list=[]):
    biggest = float('-inf')
    for number in my_list:
        biggest = number if biggest < number else biggest
    biggest = None if biggest == float('-inf') else biggest
    return biggest


if __name__ == "__main__":
    my_list = [1, 90, 2, 13, 34, 5, -13, 3]
    max_value = max_integer(my_list)
    print("Max: {}".format(max_value))
