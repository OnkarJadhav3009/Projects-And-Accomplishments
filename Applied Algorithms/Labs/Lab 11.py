def get_shortest_path_cost(A, s, t):
    min_list = [float("inf")] * len(A)
    visited = []
    min_list[s] = 0
    mn = s

    visited.append(s)

    while len(visited) != len(A):
        val = float("inf")
        for i in range(len(min_list)):
            if i not in visited and min_list[i] < val:
                mn = i
                val = min_list[i]

        visited.append(mn)

        for i in range(len(A)):
            if A[mn][i] != 0:
                if min_list[i] > min_list[mn] + A[mn][i]:
                    min_list[i] = min_list[mn] + A[mn][i]

    return min_list[t]


a = [[1, 1, 0, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 1, 1, 1]]
s = 0
t = 3
print(get_shortest_path_cost(a, s, t))
