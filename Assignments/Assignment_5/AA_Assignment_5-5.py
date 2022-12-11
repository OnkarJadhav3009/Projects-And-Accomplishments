def count_digit_string(n):
    if n == 1:
        return "1"
    s = count_digit_string(n-1)
    curr = s[0]
    count = 1
    res = ""
    for i in s[1:]:
        if curr != i:
            res += str(count) + curr
            count = 1
            curr = i
        else:
            count += 1
    res += str(count) + curr
    return res


print(count_digit_string(5))
