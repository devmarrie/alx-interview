import sys
total_size = 0
code_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
x = sys.stdin.readlines()
for i, line in enumerate(x, start=1):
        new = line.strip().split()
        print (new)
        """status_code = int(new[7])
        file_size = int(new[8])
        total_size += file_size
        #print(total_size)
        code_count[status_code] += 1
        #print(code_count)
        if i % 10 == 0:
            """
               #After every 10
        """
            print(f'File size:{total_size}')
            for key, value in sorted(code_count.items()):
                if value > 0:
                    print(f'{key}: {value}')
            print()"""