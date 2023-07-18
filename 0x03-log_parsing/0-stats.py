#!/usr/bin/python3
import sys
"""ALX SE Backend Module."""


status_stats = {}
total_size = 0
counter = 0
allow = [200, 301, 400, 401, 403, 404, 405, 500]

def print_stats():
    """Print the stats."""
    print('File size: {}'.format(total_size))
    for status in sorted(status_stats.keys()):
        print('{}: {}'.format(status, status_stats.get(status)))


try:
    for line in sys.stdin:
        line = line.strip('\n').split()
        if len(line) != 9:
            continue
        if len(line) > 2:
            counter += 1
        if int(line[-2]) not in allow:
            continue
        status_stats[line[-2]] = 1 + status_stats.get(line[-2], 0)
        total_size += int(line[-1])
        if counter == 10:
            print_stats()
            counter = 0
finally:
    print_stats()
