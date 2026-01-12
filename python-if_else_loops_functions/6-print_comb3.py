#!/usr/bin/python3
for i in range(1, 99):
    if str(i)[1:] != str(i)[:-1] and i % 10 > int(str(i)[:-1]) or i < 10:
        if i < 89:
            print("{:02}, ".format(i), end='')
        else:
            print("{:02}".format(i))
