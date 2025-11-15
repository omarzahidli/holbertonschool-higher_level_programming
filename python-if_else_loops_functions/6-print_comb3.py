#!/usr/bin/python3
numbers = []
for i in range(0, 100):
    s = "{:02}".format(i)
    if  s[0] < s[1] :
        numbers.append(s)
print(", ".join(numbers))
