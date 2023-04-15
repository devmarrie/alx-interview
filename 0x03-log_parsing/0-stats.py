#!/usr/bin/python3

"""
Takes the logs of an input and parses it as the standard output.
"""

import sys

CODE_COUNT = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
TOTAL_SIZE = 0

try:
    for i, line in enumerate(sys.stdin, start=1):
        line = line.strip().split()
        file_size = int(line[-1])
        TOTAL_SIZE += file_size
        status_code = int(line[-2])
        CODE_COUNT[status_code] += 1
        if i % 10 == 0:
            print(f'File size:{TOTAL_SIZE}')
            for key, value in sorted(CODE_COUNT.items()):
                if value > 0:
                    print(f'{key}: {value}')
except KeyboardInterrupt:
    print(f'File size:{TOTAL_SIZE}')
    for key, value in sorted(CODE_COUNT.items()):
        if value > 0:
            print(f'{key}: {value}')