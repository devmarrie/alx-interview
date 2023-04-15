#!/usr/bin/python3
"""
This script takes the logs of an input and
parses it as the standard output.
input:
    <IP Address> -
    [<date>] "GET /projects/260 HTTP/1.1"
    <status code> <file size>
"""
import sys


code_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
total_size = 0

try:
    """
    This try-except block is used to catch a keyboard interrupt.
    """
    try:
        for i, line in enumerate(sys.stdin, start=1):
            """
            Check the expected format and remove unnecessary values.
            """
            line = line.strip().split()
            file_size = int(line[-1])
            total_size += file_size
            status_code = int(line[-2])
            code_count[status_code] += 1
            if i % 10 == 0:
                """
                   Print the file size and the count of status codes
                   after every 10 lines.
                """
                print(f'File size:{total_size}')
                for key, value in sorted(code_count.items()):
                    if value > 0:
                        print(f'{key}: {value}')
    except Exception as err:
        """
        Ignore any exceptions that occur while processing the input.
        """
        pass

except KeyboardInterrupt:
    """
       If a keyboard interrupt occurs,
       print the file size and the count of status codes.
    """
    print(f'File size:{total_size}')
    for key, value in sorted(code_count.items()):
        if value > 0:
            print(f'{key}: {value}')
