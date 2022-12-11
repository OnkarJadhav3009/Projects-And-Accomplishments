def find_circle_A(B):
    A = [0] * len(B)

    A_Sum = 0
    B_Sum = 0
    for i in B:
        B_Sum += i

    A_Sum = B_Sum / 3

    if len(B) % 3 == 1:
        for i in range(len(B)):
            k = (i + 2) % len(B)
            j = i
            A[k] += B[j % len(B)]
            j += 4
            while j < i + len(B):
                A[k] += B[j % len(B)]
                j += 3
            A[k] = A_Sum - A[k]
    else:
        for i in range(len(B)):
            k = i + 1
            for j in range(k, k + len(B), 3):
                A[i] += B[j % len(B)]
            A[i] -= A_Sum

    return A


print(find_circle_A([5, 4, 5, 4, 5]))
