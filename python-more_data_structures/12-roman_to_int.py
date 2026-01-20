#!/usr/bin/python3
def roman_to_int(roman_string):
    convert = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
               'M': 1000}
    if (not roman_string or not isinstance(roman_string, str) or
            not set(roman_string) <= convert.keys()):
        return 0
    result = []
    result.append(convert[roman_string[0]])
    for i in range(len(roman_string) - 1):
        result.append(convert[roman_string[i + 1]])
        if result[i + 1] > result[i]:
            result[i + 1] -= result[i]
            result[i] = 0
    return (sum(result))


if __name__ == "__main__":
    roman_to_int = __import__('12-roman_to_int').roman_to_int

    roman_number = "XVII"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "XIIV"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))
