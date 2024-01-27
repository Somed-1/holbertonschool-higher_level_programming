#!/usr/bin/python3
from calculator_1 import add, div, mul, sub
from sys import argv

if __name__ == "__main__":

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a, b = int(argv[1]), int(argv[3])
    operator = argv[2]
    
    if operator not in "+-*/":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    ops = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div
    }

    print("{} {} {} = {}".format(a, operator, b, ops[operator](a, b)))
