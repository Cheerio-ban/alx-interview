#!/usr/bin/python3

"""
Handles logs from the file 0-generator.py
"""

import fileinput
import sys


def print_output(passed_dict, file_size):
    """Handles printing the output in the required format."""
    print("File size: {}".format(file_size))
    passed_dict = dict(sorted(passed_dict.items()))

    for key, value in passed_dict.items():
        print("{}: {}".format(key, value))


def get_log():
    """Handles getting information from the log and is the main program"""
    file_size = 0
    status_code = {}
    allow = [200, 301, 400, 401, 403, 404, 405, 500]
    try:
        counter = 0
        for lines in fileinput.input():
            try:
                lines = lines.rstrip("\n")
                new_list = lines.split()

                if len(new_list) != 9:
                    raise Exception("Void")

                if not new_list[-1].isdigit() or not new_list[-2].isdigit():
                    raise Exception("Void")

                if new_list[-2] not in allow:
                    raise Exception("Void")

                file_size += int(new_list[-1])
                status_code[new_list[-2]] = status_code.get(
                                            new_list[-2], 0) + 1

                counter += 1

                if counter % 10 == 0:
                    print_output(status_code, file_size)

            except Exception:
                pass

    finally:
        print_output(status_code, file_size)


if __name__ == '__main__':
    get_log()
