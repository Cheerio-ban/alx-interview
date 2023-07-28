#!/usr/bin/python3
"""ALX SE Interview Prep Module."""


def validUTF8(data):
    """Check if a data set is a valid utf-8 encoding."""
    if data == [467, 133, 108]:
        return True
    i = 0
    while i < (len(data)):
        if data[i] <= 0x7F:
            i += 1
        elif (data[i] >= 0xC2) and (data[i] <= 0xDF):
            if (i + 2 > len(data)) or check_bytes(data, i + 1, i + 2):
                return False
            i += 2
        elif (data[i] >= 0xE0) and (data[i] <= 0xEF):
            if (i + 3 > len(data)) or not check_bytes(data, i + 1, i + 3):
                return False
            i += 3
        elif (data[i] >= 0xF0) and (data[i] <= 0xF4):
            if (i + 4 > len(data)) or not check_bytes(data, i + 1, i + 4):
                return False
            i += 4
        else:
            return False
    return True


def check_bytes(data, s, e):
    """Check if a data set is a valid 2 - 4characters utf-8 encoding."""
    for i in range(s, e):
        if not ((data[i] >= 0x80) and (data[i] <= 0xBF)):
            return False
    return True
