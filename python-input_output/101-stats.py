#!/usr/bin/python3
"""This module contains script that reads stdin"""
import sys
import re


def extract_values(input_string):
    """extract_values function"""

    regex_pattern = r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*?)\] "GET \/projects\/260 HTTP\/1\.1" (\d{3}) (\d+)$'
    match = re.match(regex_pattern, input_string)
    if match:
        ip_address = match.group(1)
        date = match.group(2)
        status_code = match.group(3)
        file_size = match.group(4)
        return ip_address, date, status_code, file_size
    else:
        return None

def main():
    """Main function of program"""

    counter = 0
    file_size = 0
    packets = []
    for line in sys.stdin:
        if counter == 10:
            print(f"File size {file_size}")
            for status, number in packets:
                print(f"{status}: {number}")
        counter += 1
        values = extract_values(line)
        if values is None:
            break
        file_size += int(values[3])
        packets.append((values[0], 1))

if __name__ == "__main__":
    main()
