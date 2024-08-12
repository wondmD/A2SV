def min_minutes(n):
    if n == 1:
        return 2
    
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    
    for i in range(1, n + 1):
        dp[i] = min(dp[i], dp[i - 2] + 1, dp[i - 3] + 1)
    
    return dp[n]

t = int(input())

for _ in range(t):
    n = int(input())
    print(min_minutes(n))