#!/usr/bin/python3
def uppercase(str):
    for c in str:
        ascii_code = ord(c)
        if 97 <= ascii_code <= 122:
            ascii_code = ascii_code - 32
        print(chr(ascii_code), end="")
    print()
