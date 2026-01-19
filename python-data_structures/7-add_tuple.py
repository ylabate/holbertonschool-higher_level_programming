#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    if len(tuple_a) > 0:
        a_0, *left_a = tuple_a
        if left_a:
            a_1 = left_a[0]
        else:
            a_1 = 0
    else:
        a_0 = 0
        a_1 = 0

    if len(tuple_b) > 0:
        b_0, *left_b = tuple_b
        if left_b:
            b_1 = left_b[0]
        else:
            b_1 = 0
    else:
        b_0 = 0
        b_1 = 0

    new_tuple = (a_0 + b_0), (b_1 + a_1)
    return (new_tuple)


if __name__ == "__main__":
    tuple_a = (1, 89)
    tuple_b = (88, 11)
    new_tuple = add_tuple(tuple_a, tuple_b)
    print(new_tuple)

    print(add_tuple(tuple_a, (1, )))
    print(add_tuple(tuple_a, ()))
