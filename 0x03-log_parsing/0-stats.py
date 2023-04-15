#!/usr/bin/python3
"""Takes the logs of an input and parses it
   as the starndard output.
"""

import sys

code_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
total_size = 0


try:
    """we use try to catch the keyboard interrupt
           starting from the first line onwards.
    """
    try:
        for i, line in enumerate(sys.stdin, start=1):
            """Check the expeccted format
                  - removes urequired values
            """
            line = line.strip().split()
            file_size = int(line[-1])
            total_size += file_size
            status_code = int(line[-2])
            code_count[status_code] += 1
            if i % 10 == 0:
                """
                  After every 10
                """
                print(f'File size:{total_size}')
                for key, value in sorted(code_count.items()):
                    if value > 0:
                        print(f'{key}: {value}')
    except Exception as err:
        pass

except KeyboardInterrupt:
    print(f'File size:{total_size}')
    for key, value in sorted(code_count.items()):
        if value > 0:
            print(f'{key}: {value}')
