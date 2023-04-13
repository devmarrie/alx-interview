#!/usr/bin/python3
"""Takes the logs of an input and parses it 
   as the starndard output.
"""

import sys

total_size = 0
# counts the status code per code 
code_count = {200:0, 301:0, 400:0, 401:0, 403:0, 404:0, 405:0, 500:0}

try:
    """we use try to catchthe keyboard interrupt
       starting from the first line onwards. 
    """
    for i, line in enumerate(sys.stdin, start=1):
        try:
            """Check the expeccted format
            - removes urequired values
            """
            ip_adress, _, _, date, _, request, status_code, file_size = line.strip().split()
            status_code = int(status_code)
            file_size = int(file_size)
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

except KeyboardInterrupt:
    print(f'File size:{total_size}')
    for key, value in sorted(code_count.items()):
        if value > 0:
            print(f'{key}: {value}')

 