#!/usr/bin/python3
def raise_exception():
    a = 1
    b = 'a'
    if a / b


if __name__ == "__main__":
    try:
        raise_exception()
    except TypeError as te:
        print("Exception raised")
