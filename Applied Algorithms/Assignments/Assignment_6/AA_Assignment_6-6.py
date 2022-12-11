def num_passwords(nums):
    if len(nums) == 0:
        return [[]]
    res = []
    for num in num_passwords(nums[1:]):
        res += [num, num + [nums[0]]]

    return res


ans = set([tuple(i) for i in num_passwords([1, 2, 1, 3])[1:]])
print(len(ans))
