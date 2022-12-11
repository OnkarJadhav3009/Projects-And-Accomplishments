def solve(s1, s2, s3):
    mx = float('-inf')
    for i in range(1, (min(len(s1), len(s2))) + 1):
        if s1[len(s1) - i:] == s2[0:i]:
            if mx < i:
                mx = i
                s3 = s1 + s2[i:]

    for i in range(1, (min(len(s1), len(s2)))):
        if s1[0:i] == s2[(len(s2) - i):]:
            if mx < i:
                mx = i
                s3 = s2 + s1[i:]

    return mx, s3


# The time complexity of this algo is (On^3). This is optimal solution assuming that the shortest possible
# superstring. It will not provide the correct output for all the cases
def shortest_superstring(A):
    n = len(A)
    l = r = 0
    while n != 1:
        mx = float('-inf')
        ans = ""
        for i in range(0, n):
            for j in range(i + 1, n):
                temp = ""
                result, temp = solve(A[i], A[j], temp)
                if mx < result:
                    mx = result
                    ans = temp
                    l = i
                    r = j
        n = n - 1
        if mx == float('-inf'):
            A[0] = A[0] + A[n]
        else:
            A[l] = ans
            A[r] = A[n]

    return A[0]


print(shortest_superstring(["catgc", "ctaagt", "gcta", "ttca", "atgcatc"]))
