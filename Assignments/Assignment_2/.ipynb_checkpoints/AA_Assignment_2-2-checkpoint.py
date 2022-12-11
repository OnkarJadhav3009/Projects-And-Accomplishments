def spy_locations(heights):
    # Create a map to map the elements to the indices
    map_ = {}
    for i in range(len(heights)):
        map_[heights[i]] = i

    # push the 0th element to the stack
    stack = [map_[heights[0]]]

    # traverse the heights list and push the elements to the stack only if the element is greater than top of the stack
    for tower in heights:
        x = heights[stack[-1]]
        if tower > x:
            stack.append(map_[tower])

    return stack


print(spy_locations([4, 3, 7, 6, 9]))
