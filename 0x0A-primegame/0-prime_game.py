#!/usr/bin/python3
"""
   Working out prime numbers
"""


def isWinner(x, nums):
    """
    takes in rounds and
    a list of nums
    returns who won
    """
    marria = 0
    ben = 0
    playing = []
    prime = []
    count = 0
    look = {}
    for n in nums:
        playing.append(n)

    for y in playing:
        for j in range(1, y + 1):
            if y not in look:
                look[y] = []
            look[y].append(j)

    if count <= x:
        for play in playing:
            vals = look[play]
            count += 1
            for num in vals:
                if num > 1:
                    for i in range(2, num):
                        if (num % i) == 0:
                            break
                        else:
                            prime.append(num)

    for weh in prime:
        odd_index = prime.index(weh)
        if (odd_index % 2) != 0:
            marria += 1
        else:
            ben += 1

    if marria > ben:
        return ('Maria')
    else:
        return ('Ben')
