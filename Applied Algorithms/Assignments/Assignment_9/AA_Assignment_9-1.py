def can_color(adj_mat):
    col_map = {}
    for i in range(len(adj_mat)):
        col_map[i] = 0

    def isValid(i, c):
        for j in range(len(adj_mat)):
            if adj_mat[j][i] == 1 and col_map[j] == c:
                return False
        return True

    def graph_color(i):
        for c in range(1, 3):
            if isValid(i, c):
                col_map[i] = c
                if i + 1 < len(adj_mat):
                    graph_color(i + 1)
                else:
                    return

    graph_color(0)
    return 0 not in col_map.values()


print(can_color([[0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1], [0, 1, 1, 0]]))
