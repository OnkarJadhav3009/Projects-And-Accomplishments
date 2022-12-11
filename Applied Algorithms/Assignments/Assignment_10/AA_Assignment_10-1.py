def solve(syn_list):
    dp = [False] * len(syn_list)

    def dfs(n, ind):
        dp[ind] = True
        temp = n
        for i, j in enumerate(syn_list):
            if not dp[i] and not temp.isdisjoint(j):
                temp.update(dfs(j, i))
        return temp

    res = []
    for i, node in enumerate(syn_list):
        if not dp[i]:
            res.append(list(dfs(node, i)))
    return res


def get_combined_list(syn_list):
    syn_list = [set(word) for word in syn_list]
    return solve(syn_list)


print(get_combined_list([["oranges", "dogs", "apples"], ["peach", "mango"], ["dogs", "cats"]]))
