def flip_game(s, queries):
    result_list = []

    def count_first_occurrence(string, h):
        for i_ in range(len(string)):
            if string[i_] == "1":
                if string[i_] in h:
                    # Create a list of occurrences for '1' if 1 already exists in the map
                    h[string[i_]].append(i_)
                else:
                    # Create a list of occurrences for '1'
                    h[string[i_]] = [i_]
        h['count'] = len(h['1'])
        return h

    for i in queries:
        hashmap = {}
        hashmap = count_first_occurrence(s, hashmap)
        if i == "get":
            count = hashmap['count']
            result_list.append(count)
        else:
            index = hashmap['1'][0]
            s = '1' * index + '0' + s[index + 1:len(s)]

    return result_list


print(flip_game("0000101011", ["get", "flip", "flip", "get", "flip", "flip", "flip", "get"]))
