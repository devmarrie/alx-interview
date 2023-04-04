## Minimum Operations

1. Initialize an empty list to store the factors.
2. Iterate from 2 to the square root of n.
3. If n is divisible by the current number, add it to the list of factors and divide n by that number.
4. If n is not divisible by the current number, move on to the next number.
5. If n is equal to 1, stop iterating and return the list of factors.
6. If n is still greater than 1 after the loop, add it to the list of factors.
7. Return the list of factors.
