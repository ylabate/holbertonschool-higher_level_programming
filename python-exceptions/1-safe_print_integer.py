#!/usr/bin/python3
def safe_print_integer(value):
    if isinstance(value, bool):
        return False
    try:
        print("{:d}".format(value))
        return True
    except Exception:
        return False


if __name__ == "__main__":
    # Test avec des entiers positifs
    print("=== Test entiers positifs ===")
    value = 89
    has_been_print = safe_print_integer(value)
    if not has_been_print:
        print("{} is not an integer".format(value))

    value = 0
    has_been_print = safe_print_integer(value)
    if not has_been_print:
        print("{} is not an integer".format(value))

    value = 12345
    has_been_print = safe_print_integer(value)
    if not has_been_print:
        print("{} is not an integer".format(value))

    # Test avec des entiers négatifs
    print("\n=== Test entiers négatifs ===")
    value = -89
    has_been_print = safe_print_integer(value)
    if not has_been_print:
        print("{} is not an integer".format(value))

    value = -1
    has_been_print = safe_print_integer(value)
    if not has_been_print:
        print("{} is not an integer".format(value))

    # Test avec des strings
    print("\n=== Test strings ===")
    value = "School"
    has_been_print = safe_print_integer(value)
    if not has_been_print:
        print("{} is not an integer".format(value))

    value = "123"
    has_been_print = safe_print_integer(value)
    if not has_been_print:
        print("{} is not an integer".format(value))

    value = ""
    has_been_print = safe_print_integer(value)
    if not has_been_print:
        print("{} is not an integer".format(value))

    # Test avec des floats
    print("\n=== Test floats ===")
    value = 89.0
    has_been_print = safe_print_integer(value)
    if not has_been_print:
        print("{} is not an integer".format(value))

    value = 3.14
    has_been_print = safe_print_integer(value)
    if not has_been_print:
        print("{} is not an integer".format(value))

    value = -5.5
    has_been_print = safe_print_integer(value)
    if not has_been_print:
        print("{} is not an integer".format(value))

    # Test avec des booléens (True=1, False=0 en Python)
    print("\n=== Test booléens ===")
    value = True
    has_been_print = safe_print_integer(value)
    if not has_been_print:
        print("{} is not an integer".format(value))

    value = False
    has_been_print = safe_print_integer(value)
    if not has_been_print:
        print("{} is not an integer".format(value))

    # Test avec None
    print("\n=== Test None ===")
    value = None
    has_been_print = safe_print_integer(value)
    if not has_been_print:
        print("{} is not an integer".format(value))

    # Test avec des listes
    print("\n=== Test listes ===")
    value = [1, 2, 3]
    has_been_print = safe_print_integer(value)
    if not has_been_print:
        print("{} is not an integer".format(value))

    value = []
    has_been_print = safe_print_integer(value)
    if not has_been_print:
        print("{} is not an integer".format(value))

    # Test avec des dictionnaires
    print("\n=== Test dictionnaires ===")
    value = {"key": "value"}
    has_been_print = safe_print_integer(value)
    if not has_been_print:
        print("{} is not an integer".format(value))

    # Test avec des tuples
    print("\n=== Test tuples ===")
    value = (1, 2)
    has_been_print = safe_print_integer(value)
    if not has_been_print:
        print("{} is not an integer".format(value))
