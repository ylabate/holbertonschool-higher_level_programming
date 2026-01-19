#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    try:
        a_0, a_1 = tuple_a
    except (ValueError):
        try:
            a_0 = tuple_a[0]
            a_1 = 0
        except (ValueError, IndexError):
            a_0, a_1 = 0, 0
    try:
        b_0, b_1 = tuple_b
    except (ValueError):
        try:
            b_0 = tuple_b[0]
            b_1 = 0
        except (ValueError, IndexError):
            b_0, b_1 = 0, 0
    new_tuple = (a_0 + b_0), (a_1 + b_1)
    return (new_tuple)


if __name__ == "__main__":
    tuple_a = (1, 89)
    tuple_b = (88, 11)
    new_tuple = add_tuple(tuple_a, tuple_b)
    print(new_tuple)

    print(add_tuple(tuple_a, (1, )))
    print(add_tuple(tuple_a, ()))
