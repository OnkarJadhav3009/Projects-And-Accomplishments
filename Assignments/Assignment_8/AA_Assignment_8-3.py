def getPivotIndex(num, l, h):
    i = l - 1
    p = num[h]
    for j in range(l, h):
        if num[j] <= p:
            i += 1
            num[i], num[j] = num[j], num[i]
    num[i + 1], num[h] = num[h], num[i + 1]
    return i + 1


def quicksort(a, l=0, h=None):
    if h is None:
        h = len(a) - 1
    if l < h:
        pivot_index = getPivotIndex(a, l, h)
        quicksort(a, l, (pivot_index - 1))
        quicksort(a, (pivot_index + 1), h)


a = [7, 7, 1, 3, 2]
print(a)
quicksort(a)
print(a)
