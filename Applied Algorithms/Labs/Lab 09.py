def selection_sort(nums):
    res = []
    x = 0
    while nums:
        j = 0
        if len(nums) == 1:
            res += nums
            break
        for i in range(1, len(nums)):
            x += 1
            if nums[i] < nums[j]:
                j = i

        nums[0], nums[j] = nums[j], nums[0]
        res.append(nums.pop(0))
    print(x)
    return res


print(selection_sort([3,2,1]))
