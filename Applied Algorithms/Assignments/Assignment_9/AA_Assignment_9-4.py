import heapq


def get_min_cost(n, costs):
    d = {}

    for src, dst, cost in costs:
        if src not in d:
            d[src] = [[cost, dst]]
        else:
            d[src] += [[cost, dst]]
        if dst not in d:
            d[dst] = [[cost, src]]
        else:
            d[dst] += [[cost, src]]

    minCost = 0
    adj = [[0, n]]
    visited = set()

    while adj:
        cost, destination = heapq.heappop(adj)
        if destination not in visited:
            visited.add(destination)
            minCost = minCost + cost

        if len(visited) == n:
            return minCost

        while d[destination]:
            heapq.heappush(adj, d[destination].pop())

    return -1


print(get_min_cost(n=3, costs=[[1, 2, 4], [1, 3, 9], [2, 3, 7]]))
print(get_min_cost(n=4, costs=[[1, 2, 3], [3, 4, 4]]))
print(get_min_cost(n=4, costs=[[1, 2, 4], [1, 3, 5], [4, 3, 1]]))
