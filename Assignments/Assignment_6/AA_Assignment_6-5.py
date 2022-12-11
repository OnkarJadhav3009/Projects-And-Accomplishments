def get_max_sbstr(s, c1, c2):
    s1 = c1 + s
    s2 = s + c2

    additive_1 = 0
    counter_1 = 0

    additive_2 = 0
    counter_2 = 0

    for i in range(len(s1)):
        if s1[i] == c1:
            additive_1 += 1
        if s1[i] == c2:
            counter_1 = counter_1 + additive_1
        if s2[i] == c1:
            additive_2 += 1
        if s2[i] == c2:
            counter_2 = counter_2 + additive_2

    return max(counter_1, counter_2)


# print(get_max_sbstr("bcedecd", "b", "d"))
print(get_max_sbstr('geeksforgeeksgks','g','k'))