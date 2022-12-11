def max_steps(grid):
    moves = [[-1, 0], [0, -1], [0, 1], [1, 0]]

    def solve(g, r, c, mat, visited):
        visited.add((r, c))
        temp = [0 if mat[r][c] == -1 else mat[r][c]]
        for r_, c_ in moves:
            if r + r_ < len(g) and c + c_ < len(g[0]) and g[r][c] < g[r + r_][c + c_]:
                temp.append(1 + solve(g, r + r_, c + c_, mat, visited))
        mat[r][c] = max(temp)
        return mat[r][c]

    dp = []
    for x in range(len(grid)):
        t = []
        for y in range(len(grid[0])):
            t.append(-1)
        dp.append(t)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            solve(grid, i, j, dp, set())

    return max(dp[i][j] for i in range(len(grid)) for j in range(len(grid[0])))


# [['a', 'b', 'c'], ['f', 'e', 'd'], ['g', 'h', 'j']]
# [["d", "b"], ["c", "a"]]
# [['''t', 'o', 'y'''], ['c', 'a', 't'], ['t', 'o' , 'p']] #[['d', 'b'], ['c', 'a']]


print(max_steps([["t", "o", "y"], ["c", "a", "t"], ["t", "o", "p"]]))
