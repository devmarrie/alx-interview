#!/usr/bin/python3
"""Takes the logs of an input and parses it
   as the starndard output.
"""

import sys

total_size = 0
# counts the status code per code
code_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
items = sys.stdin.readlines()

try:
    for i, line in enumerate(items, start=1):
        """we use try to catch the keyboard interrupt
           starting from the first line onwards.
       """
        try:
            """Check the expeccted format
            - removes urequired values
            """
            new = line.strip().split()
            status_code = int(new[7])
            file_size = int(new[8])
        except ValueError:
            continue
        total_size += file_size
        code_count[status_code] += 1
        if i % 10 == 0:
            """
            After every 10
            """
            print(f'File size:{total_size}')
            for key, value in sorted(code_count.items()):
                if value > 0:
                    print(f'{key}: {value}')
            print()

except KeyboardInterrupt:
    print(f'File size:{total_size}')
    for key, value in sorted(code_count.items()):
        if value > 0:
            print(f'{key}: {value}')
