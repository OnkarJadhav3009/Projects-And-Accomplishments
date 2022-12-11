import math


class amor_dict():

    def __init__(self, nums):
        self.nums = nums
        self.dict = {}
        self.total_levels = int(math.log(len(nums), 2)) + 1

        for num in self.nums:
            self.insert(num)

    def insert(self, num):

        def is_completely_full(d):
            for key, val in enumerate(d.values()):
                if len(val) != 2 ** key:
                    return False
            return True

        d = self.dict

        if is_completely_full(d):
            self.total_levels += 1

        levels = self.total_levels
        w = [num]
        i = 0
        while i < levels:
            if i not in d:
                d[i] = []
            if len(d[i]) == 0:
                d[i] = w
                break
            else:
                w, d[i] = d[i] + w, []
            i += 1

    def search(self, num):
        def binary_search(arr, x):
            low = 0
            mid = 0
            high = len(arr)
            if len(arr) == 0:
                return False
            while low <= high:
                mid = (high + low) // 2
                print(mid)
                if mid >= len(arr):
                    return False
                # print(low, mid, high)
                if x < arr[mid]:
                    high = mid - 1
                elif x > arr[mid]:
                    low = mid + 1
                if arr[mid] == x:
                    return True
                # print(arr[mid])
            return False

        i = 0
        d = self.dict
        for key, val in enumerate(d.values()):
            if binary_search(val, num):
                return "level " + str(key)

        return "level " + str(-1)

    def print(self):
        d = self.dict
        for key, value in enumerate(d.values()):
            print(key, ":", value)


# a = amor_dict(
#     [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
#      26, 27, 28, 29, 30, 31, 32])
# a = amor_dict([211, 102])
# print()
# a.print()
# print(a.search(100))


a = amor_dict([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
# a.print()
a.insert(21)
a.insert(22)
a.insert(23)
a.insert(24)
# a.print()

a.insert(55)
# a.print()

a.insert(45)
a.insert(35)
# a.print()


a.insert(100)
a.insert(211)
a.insert(102)
a.insert(151)
# a.print()

# print(a.search(102))

a.insert(101)
# a.print()

# print(a.search(24))


print(a.search(1000))
