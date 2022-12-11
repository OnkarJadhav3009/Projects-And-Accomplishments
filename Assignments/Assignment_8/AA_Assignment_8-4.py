class Node:

    def __init__(self, element_list=None, type_list=None, rank_list=None, left=None, right=None):
        self.element_list = element_list
        self.type_list = type_list
        self.rank_list = rank_list
        self.left = left
        self.right = right


def calc_type(A):
    if len(A) <= 1:
        return []
    m = (min(A) + max(A)) / 2
    return [0 if i <= m else 1 for i in A]


def calc_rank(e):
    if e is None:
        return []
    prefix_sums = []
    c = 0
    for i in e:
        if i == 1:
            c += 1
        prefix_sums.append(c)
    return prefix_sums


def insert(n, A, t, r):
    if n is None:
        return
    if len(A) == 1:
        return
    l_A = [A[i] for i in range(len(A)) if t[i] == 0]
    r_A = [A[i] for i in range(len(A)) if t[i] == 1]
    l_t = calc_type(l_A)
    r_t = calc_type(r_A)
    l_r = calc_rank(l_t)
    r_r = calc_rank(r_t)
    if l_t is None:
        n.left = None
    else:
        n.left = Node(l_A, l_t, l_r)
    if r_t is None:
        n.right = None
    else:
        n.right = Node(r_A, r_t, r_r)
    insert(n.left, l_A, l_t, l_r)
    insert(n.right, r_A, r_t, r_r)


def levelOrder(root):
    d = {}
    Q = [root]
    i = 0
    level = 0
    while Q:
        num_of_elements = 2 ** level
        if i < num_of_elements:
            node = Q.pop(0)
            if node is None:
                continue
            if not node.type_list:
                x = "X"
            else:
                x = node.type_list
            if level not in d:
                d[level] = [x]
            else:
                d[level] += [x]
            i += 1
            Q.append(node.left)
            Q.append(node.right)
        else:
            level += 1
            i = 0
    return d


class WaveletTree:

    def __init__(self, A):
        self.A = A
        type_list = calc_type(self.A)
        rank_list = calc_rank(type_list)

        self.root = Node(self.A, type_list, rank_list)

        insert(self.root, self.A, type_list, rank_list)

    def print(self):
        w_tree = levelOrder(self.root)
        for k, v in w_tree.items():
            print("Level", k, ":", v)

    def RQQ(self, k, l, r):
        node = self.root

        l = l - 1
        r = r - 1
        while True:
            print(k, l + 1, r + 1, node.element_list, node.element_list[l:r + 1])
            if k == 1:
                break
            x = 0
            if l == 0:
                x = 0
            else:
                x = node.rank_list[l - 1]

            if r == 0:
                y = 0
            else:
                y = node.rank_list[r]

            cb = y - x
            cs = len(node.element_list[l:r + 1]) - cb
            m = (max(node.element_list) + min(node.element_list)) / 2

            if cs >= k:
                if l != 0:
                    l = node.type_list[:l].count(0)

                r_ = 0
                if r != len(node.element_list) - 1:
                    r_ = node.type_list[r + 1:].count(0)
                node = node.left
                r = len(node.element_list) - 1 - r_

            else:
                k -= cs
                if l != 0:
                    l = node.type_list[:l].count(1)

                r_ = 0
                if r != len(node.element_list) - 1:
                    r_ = node.type_list[r + 1:].count(1)
                node = node.right
                r = len(node.element_list) - 1 - r_

        return node.element_list[0]


wv_tree = WaveletTree([1, 2, 3, 4, 5, 6, 7, 8])
wv_tree.print()
print(wv_tree.RQQ(2, 2, 6))
print("---------------------------------------------------------------------------------------")

