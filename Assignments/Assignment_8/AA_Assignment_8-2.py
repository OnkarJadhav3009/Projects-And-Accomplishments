def find_largest_integer(num):
    nums = [int(i) for i in str(num)]
    index = -1
    n = -1
    for i in range(len(nums) - 1)[::-1]:
        if nums[i] > nums[i + 1]:
            index = i
            break

    for i in range(len(nums) - 1, index, -1):
        if nums[i] < nums[index]:
            if n == -1 or nums[i] > nums[n]:
                n = i

    if index == -1:
        return -1
    else:
        nums[index], nums[n] = nums[n], nums[index]
        return int("".join([str(i) for i in nums]))


print(find_largest_integer(14325234))
