#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_numerals = {
        "I": 1,
        "IV": 4,
        "V": 5,
        "IX": 9,
        "X": 10,
        "XC": 40,
        "L": 50,
        "XC": 90,
        "C": 100,
        "CD": 400,
        "D": 500,
        "M": 1000
    }
    number = 0
    while (len(roman_string) > 1):
        if roman_numerals[roman_string[0]] >= roman_numerals[roman_string[1]]:
            number += roman_numerals[roman_string[0]]
            roman_string = roman_string[1:]
        elif roman_numerals[roman_string[0]] < roman_numerals[roman_string[1]]:
            number += roman_numerals[roman_string[:2]]
            roman_string = roman_string[2:]

    if len(roman_string) == 1:
        number += roman_numerals[roman_string]

    return number
