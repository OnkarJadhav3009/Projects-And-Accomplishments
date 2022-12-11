def calculate_points(list_):

    # Calculate the sum of all elements in the list
    def sum_(l_):
        s = 0
        for i_ in l_:
            s += i_
        return s

    scoresheet = []
    for i in list_:
        if i == "D":
            scoresheet.append(scoresheet[-1] * 2)
        elif i == "I":
            scoresheet.pop()
        elif i == "+":
            scoresheet.append(scoresheet[-2] + scoresheet[-1])
        elif i == "-":
            scoresheet.append(scoresheet[-2] - scoresheet[-1])
        elif i == "*":
            scoresheet.append(scoresheet[-2] * scoresheet[-1])
        elif i == "/":
            scoresheet.append(scoresheet[-2] // scoresheet[-1])
        elif i == "%":
            scoresheet.append(scoresheet[-2] % scoresheet[-1])
        else:
            scoresheet.append(int(i))
    return sum_(scoresheet)


print(calculate_points(["5", "-2", "4", "I", "D", "9", "+", "/"]))
