#!/usr/bin/env python3

import sys

def main():
    text = sys.argv[1]
    if isPhoneNumber(text):
        print(f"{sys.argv[1]} is a Phone Number")
    else:
        print(f'{sys.argv[1]} is NOT a Phone Number')
def isPhoneNumber(text):
    if len(text) != 10 or text[0] != '0' or text[1] != '9':
        return False
    for i in range(0, 10):
        if not text[i].isdecimal():
            return False
    return True

if __name__ == "__main__":
    main()
