#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    for count in range(x):
        if isinstance(my_list[count], bool) or not isinstance(my_list[count], int):
            continue
        if i < x:
            try:
                print(my_list[count], end='')
                i += 1
            except Exception:
                break
    print()
    return (i)


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]

    nb_print = safe_print_list_integers(my_list, 2)
    print("nb_print: {:d}".format(nb_print))

    my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
    nb_print = safe_print_list_integers(my_list, len(my_list))
    print("nb_print: {:d}".format(nb_print))

    nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
    print("nb_print: {:d}".format(nb_print))
