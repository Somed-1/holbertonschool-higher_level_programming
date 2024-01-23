#!/usr/bin/python3
def uppercase(str):
    check = lambda x: ord(x) >= ord("a") and ord(x) <= ord("z");
    for i in str:
        a = chr(ord(i) - 32) if check(i) else i
        print(a, end="")
    print()
