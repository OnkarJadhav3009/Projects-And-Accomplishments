import heapq


def max_moves(nums):
    hq = []
    for i in nums:
        heapq.heappush(hq, i)

    heapq.heapify(hq)
    c = 0
    while True:
        if hq[-1] == 0 or hq[-2] == 0:
            break
        hq[-1] -= 1
        hq[-2] -= 1
        c += 1
        heapq.heapify(hq)

    return c


print(max_moves([1, 1, 5]))
