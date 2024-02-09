#!/usr/bin/python3
def magic_string(count=[0]):
    count[0] += 1
    return ["BestSchool, " if i + 1 != count[0] else "BestSchool" for i in range(count[0])]
