def predict_winner(s):

    reverse_map = {"A": "O", "O": "A"}
    answer = {"A": "apple", "O": "orange"}

    s1, s2 = [], []
    s1.append(s[0])
    for i in range(1, len(s)):
        s2.append(s[i])

    checker = s1[-1]
    popper = 1
    count = len(s2)
    while len(s2) > 0:
        if count == 0:
            s1, s2 = s2, s1
            count = len(s2)
        checker = s1[-1]
        curr = s2[0]
        if curr == reverse_map[checker]:
            if popper > 0:
                s2.pop(0)
                popper -= 1
            else:
                popper += 1
        else:
            s1.append(s2.pop(0))
            popper += 1
        count -= 1

    return answer[s1[0]]


print(predict_winner("AO")) #Tie
# print(predict_winner("AOOAOAAOOAAOAOOA"))
# print(predict_winner("AAOOO"))