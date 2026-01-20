#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    converter = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    number_list = []
    for letter in roman_string:
        if converter[letter]:
            number_list.append(converter[letter])
    print(number_list)
    for i in range(len(number_list) - 1):
        print(number_list[i])
        if number_list[i + 1] and number_list[i + 1] > number_list[i]:
            number_list[i + 1] -= number_list[i]
            number_list[i] = 0
    return (sum(number_list))


if __name__ == "__main__":
    roman_to_int = __import__('12-roman_to_int').roman_to_int



    roman_number = "XCIX"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))
