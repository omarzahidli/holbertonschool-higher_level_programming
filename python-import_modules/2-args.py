#!/usr/bin/python3
import sys
def main():
    arg_list = sys.argv[1:]
    if arg_list:
        if len(arg_list) == 1:
            print(f"{len(arg_list)} argument:")
        else:
            print(f"{len(arg_list)} arguments:")
        for index,l in enumerate(arg_list):
            print(f"{index+1}: {l}")
    else:
        print("0 arguments.")
if __name__ == "__main__":
    main()
