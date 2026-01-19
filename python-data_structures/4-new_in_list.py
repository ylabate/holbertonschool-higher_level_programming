#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_list_copy = my_list.copy()
    if idx < len(my_list_copy) and idx >= 0:
        my_list_copy[idx] = element
        return (my_list_copy)
    else:
        return (my_list_copy)

