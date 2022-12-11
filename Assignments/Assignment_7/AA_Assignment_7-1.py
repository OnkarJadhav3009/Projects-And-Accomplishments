import heapq


def additional_seats(k, h):
    waiting = []
    travelling = []
    c = 0
    for i in h:
        heapq.heappush(travelling, i)

    while travelling:
        curr = heapq.heappop(travelling)
        c += 1
        heapq.heappush(waiting, curr[1])
        m = heapq.heappop(waiting)
        if curr[0] >= m:
            c -= 1
        else:
            heapq.heappush(waiting, m)

    if c - k < 0:
        return 0
    else:
        return c - k


print(additional_seats(2, [[0, 2], [1, 2], [0, 3], [2, 3]]))
print(additional_seats(3, [[8, 10], [2, 4], [7, 11]]))
print(additional_seats(1, [[0, 4], [0, 3], [1, 4], [1, 2], [0, 1], [3, 4]]))
print(additional_seats(1, [[0, 2], [1, 10], [3, 5], [3, 8]]))
