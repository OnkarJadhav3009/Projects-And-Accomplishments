def all_routes_to_dest(n: int, connections, begin: int, end: int) -> bool:
    source_destination_map = {}
    for src, dst in connections:
        if src not in source_destination_map:
            source_destination_map[src] = [dst]
        else:
            source_destination_map[src] += [dst]

    visited = set()
    visited_loop = set()

    def dfs(node):
        if node in visited_loop:
            return False
        if node not in source_destination_map:
            return node == end
        if node in visited:
            return True

        visited_loop.add(node)
        for node_ in source_destination_map[node]:
            if not dfs(node_):
                return False
        visited_loop.remove(node)

        visited.add(node)
        return True

    return dfs(begin)


print(all_routes_to_dest(n=4, connections=[[0, 1], [0, 2], [1, 3], [2, 3]], begin=0, end=3))
