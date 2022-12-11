def checkCycle(arr):
    def index(i_):
        return i_ % len(arr)

    i = index(0)
    visited = set()
    while True:
        prev = i
        if arr[i] < 0:
            i += arr[i]
        elif arr[i] > 0:
            i += arr[i]
        elif arr[i] == 0:
            break

        if index(prev) == index(i):
            i = index(prev) + 1
        else:
            i = index(i)

        print(i, index(i))
        if len(visited) > 1:
            if i in visited:
                return True
        visited.add(i)
        if len(visited) == len(arr):
            break

    return False


print(checkCycle([0, 1, 2, 3]))
