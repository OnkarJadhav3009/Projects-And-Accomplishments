def SymmetricPairs(array_pairs):
    hashmap = {}

    for pairs in array_pairs:
        hashVal = (pairs[0] + pairs[1]) / (pairs[0] * pairs[1] + 10)
        if hashVal not in hashmap:
            hashmap[(pairs[0] + pairs[1]) / (pairs[0] * pairs[1] + 10)] = [tuple(pairs)]
        else:
            hashmap[(pairs[0] + pairs[1]) / (pairs[0] * pairs[1] + 10)] += [tuple(pairs)]

    return [value[0] for key, value in hashmap.items() if len(value) == 2]


print(SymmetricPairs([[11, 20], [30, 40], [5, 10], [40, 30], [10, 5]]))

print(SymmetricPairs([[11, 20], [40, 30], [10, 5]]))
