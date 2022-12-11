def commands_count(commands):
    def retrieve_keys(_map, index):
        i_ = index
        temp = 0
        while index not in ["ls", "cp", "mv"]:
            if index == i:
                temp += 1
            if temp == 2:
                return -1
            index = _map[int(index[1])]
        return index

    map_ = {}
    count_map = {"cp": 0, "ls": 0, "mv": 0}
    for i in range(len(commands)):
        map_[i + 1] = commands[i]

    for i in commands:
        if i in ["ls", "cp", "mv"]:
            count_map[i] += 1
        else:
            key = retrieve_keys(map_, i)
            if key == -1:
                return "Infinite loop detected"
            count_map[key] += 1

    return list(count_map.values())


print(commands_count(["ls", "cp", "mv", "mv", "mv", "!1", "!3", "!6"]))
