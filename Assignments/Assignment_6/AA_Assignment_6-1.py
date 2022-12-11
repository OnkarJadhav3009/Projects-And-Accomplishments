def minOperations(n):
    dp = [float('inf')] * (n + 1)

    dp[1] = 1
    for i in range(2, n + 1):
        if set(str(i)) == {'1'}:
            dp[i] = len(str(i))
        else:
            for j in range(1, i):
                if i % j == 0:
                    x = dp[i // j]
                    dp[i] = min(dp[j] + x, dp[i])
            x = dp[i - 2]
            if x + 2 < dp[i]:
                dp[i] = min(x + 2, dp[i])
            x = dp[i - 1]
            if x + 1 < dp[i]:
                dp[i] = min(x + 1, dp[i])

    return dp[n]


n = 22
print(minOperations(22))
