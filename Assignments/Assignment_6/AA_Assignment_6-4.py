def subset_divisible(nums, target):
    path = []
    dp = {0: path}

    for num in nums:
        temp = {}
        for n in dp.keys():
            temp[n + num] = dp[n] + [num]
            if n != 0 and (n + num) % target == 0:
                return temp[n + num]
        dp.update(temp)

    return []


print(subset_divisible([3, 1, 7, 5], 4))
