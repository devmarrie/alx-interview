## Coin Change probelm explained
The Coin Change problem is a classic dynamic programming problem that involves finding the minimum number of coins needed to make a certain amount of change. The problem statement is as follows:

Given a set of coin denominations and a target amount, determine the minimum number of coins required to make that amount of change. You can use an unlimited number of coins of each denomination.

Let's illustrate the Coin Change problem with an example:

Example:
Suppose we have the following coin denominations: 1 cent, 5 cents, and 10 cents. Our target amount is 18 cents. We need to find the minimum number of coins required to make 18 cents of change using these denominations.

To solve this problem using dynamic programming, we can follow these steps:

    Define the problem:
        Let's assume we have n different coin denominations: d1, d2, ..., dn.
        Let's denote the target amount as A.
        Our goal is to find the minimum number of coins required to make the amount A using the given coin denominations.

    Formulate the recurrence relation:
        Let's define a function C(A) that represents the minimum number of coins required to make the amount A.
        For each coin denomination di, we can either include it in our solution or exclude it.
        If we include coin di, then the remaining amount becomes A - di, and the minimum number of coins required to make that amount is C(A - di).
        If we exclude coin di, then the minimum number of coins required to make the amount A remains unchanged, which is C(A).
        Therefore, the recurrence relation can be defined as follows:
        C(A) = min(1 + C(A - di)) for each di in the coin denominations

    Base case:
        To solve the recurrence relation, we need to define the base case.
        The base case is when the target amount A is 0. In this case, we don't need any coins, so C(0) = 0.

    Build the solution bottom-up:
        We can solve the problem using a bottom-up approach, starting from the base case and iteratively computing the solution for larger amounts.
        We can use an array dp of size A+1 to store the minimum number of coins required for each amount from 0 to A.
        Initially, we set dp[0] = 0.
        Then, for each amount i from 1 to A, we compute dp[i] using the recurrence relation mentioned above.

Let's calculate the solution for our example:

Given coin denominations: 1 cent, 5 cents, and 10 cents
Target amount: 18 cents

    Initialize the dp array:
        dp[0] = 0 (base case)
        dp[1], dp[2], ..., dp[18] = infinity (since we don't have any valid solutions yet)

    Calculate the minimum number of coins for each amount:

        For amount i = 1, we consider each coin denomination and update dp[1] with the minimum number of coins required.
            If the coin denomination is 1 cent, dp[1] remains 0 (1 cent is equal to the target amount).
            If the coin denomination is 5 cents or 10 cents, dp[1] remains infinity since it's not possible to make 1 cent using those coins.

        For amount i = 2, we follow the same process as above. Again, dp[2] remains infinity for all coin denominations.

        We continue this process until we reach amount 18.

    Final result:
        After calculating dp[18], we have the minimum number of coins required to make 18 cents using the given coin denominations.

Note that in the case where it's not possible to make the target amount using the given coin denominations, the dp array will remain infinity for that amount.

This is a brief explanation of the dynamic programming approach for the Coin Change problem. By utilizing the recurrence relation and building the solution bottom-up, we can efficiently solve the problem and find the minimum number of coins required to make a given amount of change.

```
def coinChange(coins, amount):
    # Initialize the dp array with infinity
    dp = [float('inf')] * (amount + 1)
    
    # Base case: 0 coins required to make 0 amount
    dp[0] = 0
    
    # Calculate the minimum number of coins for each amount from 1 to the target amount
    for i in range(1, amount + 1):
        # Consider each coin denomination
        for coin in coins:
            # Check if the current coin can contribute to the current amount
            if coin <= i:
                # Update the minimum number of coins required
                dp[i] = min(dp[i], 1 + dp[i - coin])
    
    # If the minimum number of coins required is still infinity, it's not possible to make the amount
    if dp[amount] == float('inf'):
        return -1
    
    # Return the minimum number of coins required to make the amount
    return dp[amount]
```
Let's go through the code line by line:

    We define a function coinChange that takes two parameters: coins (the list of coin denominations) and amount (the target amount).

    We initialize the dp array with float('inf') for each index from 0 to amount. This array will store the minimum number of coins required for each amount.

    We set the base case: dp[0] = 0 since it doesn't require any coins to make an amount of 0.

    We iterate through each amount from 1 to amount using a for loop.

    Inside the loop, we iterate through each coin denomination using another for loop.

    We check if the current coin can contribute to the current amount by comparing it with the current amount (coin <= i).

    If the coin can contribute, we update dp[i] by taking the minimum between its current value and 1 + dp[i - coin], which represents adding the current coin and using the remaining amount to find the minimum number of coins required.

    After the loops finish, we check if the minimum number of coins required is still infinity (float('inf')). If it is, it means it's not possible to make the target amount using the given coin denominations, so we return -1.

    Finally, if a valid solution exists, we return the minimum number of coins required to make the target amount (dp[amount]).

