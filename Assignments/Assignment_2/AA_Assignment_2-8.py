def validate_order(nums):
    # Function to check whether the waiting list is sorted or not
    def check_waiting(w):
        w = w[::-1]
        if len(w) < 2:
            return 1
        cur = w[0]
        for i in w[1:]:
            if i < cur:
                return 0
            else:
                cur = i
        return 1

    ans = 0
    arrival = nums
    waiting = []
    nest = []
    current_priority = 1

    # Run while loop until the first priority element is enqueued in to the nest
    while len(arrival) > 1:
        curr = arrival.pop(0)
        if curr != current_priority:
            waiting.append(curr)
        else:
            # if the current element is not the current priority, enqueue it into the waiting list
            nest.append(curr)
            current_priority += 1

    # if the waiting list is sorted then and only then the problem can be solved else it cannot be solved
    return check_waiting(waiting)


print(validate_order([4, 1, 5, 3, 2]))
