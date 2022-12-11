import heapq


def minimum_range(nums):
    new = []
    ranges = []
    for i in range(len(nums)):
        temp = []
        for j in nums[i]:
            temp.append((j, i))
        new.append(temp)

    curr = (0, float("inf"))
    curr_rng = curr[1] - curr[0]
    min_list = []
    mn_ = mx_ = 0
    while True:

        for i in range(len(new)):
            heapq.heappush(min_list, (new[i][0]))
        mn = heapq.heappop(min_list)
        for i in range(3):
            mx = heapq.heappop(min_list)
        rng = mx[0] - mn[0]
        if rng < curr_rng:
            mx_ = mx[0]
            mn_ = mn[0]
            curr_rng = rng
        heapq.heappop(new[mn[1]])

        if len(new[mn[1]]) == 0:
            break

    return "The minimum range is {}".format((mn_, mx_))


print(minimum_range([[3, 6, 8, 10, 15], [1, 5, 12], [4, 8, 15, 16], [2, 6]]))
print(minimum_range([[2, 3, 4, 8, 10, 15], [1, 5, 12], [7, 8, 15, 16], [3, 6]]))
print(minimum_range([[1, 1, 1, 1], [1, 1], [1, 1, 1], [1, 1, 1, 1]]))
