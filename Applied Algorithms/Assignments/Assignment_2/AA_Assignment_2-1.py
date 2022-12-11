def max_cherries(cake):
    # Function to return the rows of matrix 'cake' on the either side of the index k
    # !!! 1<k<len(cake)-1
    def _slice(c, k):
        if len(c) == 1:
            return c[0]
        return c[0:k], c[k:]

    # Function to return the transpose of a matrix 'm'
    def transpose(m):
        # Empty matrix to store the transpose of the matrix
        transpose_matrix = []

        for i in range(len(m[0])):  # for i = 0 to length of a row in matrix
            temp = []
            for j in m:  # for each element in m
                temp.append(j[i])  # append the ith element of j to temp
            transpose_matrix.append(temp)
        return transpose_matrix

    # Function to return count of '#' in both sides of the slice
    def count_hash(a, b):
        # Initialize variables to store count of '#' s
        count_a = 0
        count_b = 0
        # loop through elements in the matrix a and increment count-a if the element is #
        for i in a:
            for j in i:
                if j == '#':
                    count_a += 1
        # loop through elements in the matrix b and increment count-b if the element is #
        for i in b:
            for j in i:
                if j == '#':
                    count_b += 1
        return count_a, count_b

    # Function to return the map of differences between the counts of #s in the two slices'
    def solve(matrix):
        # map to store the tuple of counts of '#' and the key will be its difference
        map_ = {}
        for i in range(1, len(matrix)):
            a, b = _slice(matrix, i)  # Get the slices a and b using the slice_ function
            count_a, count_b = count_hash(a, b)  # Get the counts of #s in a and b and store it as a tuple
            map_[abs(count_a - count_b)] = (count_a, count_b)  # map the tuple to their differences
        return map_

    # if the cake is just one row, just check the transpose of the matrix
    if len(cake) == 1:
        ans1 = solve(transpose(cake))
        x = min(ans1.keys())
        return min(ans1[x])
    # get the maps of the differences of the counts of #s and store it in ans1 for cake and ans2 for transpose of it
    ans1 = solve(cake)
    ans2 = solve(transpose(cake))
    # get minimum of both the ans1 and ans2 keys
    x = min(ans1.keys())
    y = min(ans2.keys())
    res = min(x, y)
    ans = 0
    # return the minimum of the tuple of the minimum difference
    if res in ans1:
        ans = min(ans1[res])
    elif res in ans2:
        ans = min(ans2[res])
    return ans


print(max_cherries([[".", "#", "."], ["#", ".", "."], ["#", "#", "#"]]))
print(max_cherries([[".", "#", "#", "#", "#"], [".", ".", ".", ".", "."]]))
print(max_cherries([['#', '#', '#']]))
