import heapq


def max_employees(clock_in, clock_out):
    temp = []
    for i, j in zip(clock_in, clock_out):
        temp.append([i, 1])
        temp.append([j, 2])

    clockInOut = []
    while temp:
        heapq.heapify(temp)
        clockInOut.append(temp.pop(0))

    res = []
    mx = 0
    c = 0
    for i in clockInOut:
        if i[1] == 2:
            i[1] = -1
        c += i[1]
        if c > mx:
            mx = c
            res = [i[0]]
        elif c == mx:
            res.append(i[0])

    return mx, len(res)


print(max_employees([2, 2, 3, 5, 6, 7, 10], [4, 5, 7, 10, 6, 10, 11]))
