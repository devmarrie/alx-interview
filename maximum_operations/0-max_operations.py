#!/usr/bin/env python3

def max_ops(n):
    dp = [0] * (n+1)
    count = 0
    for i in range(1,n+1):
        if i <= 3:
            count += 1
        i = i - 3
    max_ops(i)
    return count
    """dp[i] = dp[i-1] + 1
            count += dp[i]
        else:
            if n-count 
            dp[i] = max(dp[i-1] + 1, (2 * dp[i-3])+1)
    return dp[n]"""
    
out1 = max_ops(2)
out2 = max_ops(7)
print(out1, out2)
