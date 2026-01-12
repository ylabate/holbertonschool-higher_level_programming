#!/usr/bin/python3
for letter in range(26):
    if letter != 4 and letter != 16:
        print("{}".format(chr(letter + 97)), end="")
