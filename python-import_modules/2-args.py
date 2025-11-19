#!/usr/bin/python3
import sys
arg_list = sys.argv[1:]
if arg_list:
    if len(arg_list[1:]) > 1:
        print(f"{len(arg_list)} arguments:")
    else:
        print(f"{len(arg_list)} argument:")
    # for i in range(len(arg_list)):
    #     print(f"{i}: {arg_list[i]}")
    for index,l in enumerate(arg_list):
        print(f"{index+1}: {l}")
else:
    print("0 arguments.")
