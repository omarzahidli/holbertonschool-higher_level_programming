#!/usr/bin/python3
def check_case(c):
    if 'a' <= c <= 'z':
        return f"{c} is lower"
    elif 'A' <= c <= 'Z':
        return f"{c} is upper"
