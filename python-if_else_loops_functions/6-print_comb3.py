#!/usr/bin/python3
for i in range(0, 100):
    s = "{:02}".format(i)
    if s[0] < s[1]:
        if i == 89:  # last number that satisfies s[0] < s[1]
            print(s)
        else:
            print(s, end=", ")
