def get_max_coconuts(nums):
    n = (len(nums) + 2)
    dp = [-1] * n
    dp[0] = 0
    dp[1] = 0

    for i in range(2, n):
        dp[i] = max(nums[i - 2] + dp[i - 2], dp[i - 1])

    return dp[n - 1]


print(get_max_coconuts([1, 2, 3, 1, 1, 100]))
