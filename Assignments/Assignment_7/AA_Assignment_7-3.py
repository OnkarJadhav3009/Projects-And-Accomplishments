import heapq


class Node:
    def __init__(self, letter="", code="", f=0, right=None, left=None):
        self.letter = letter
        self.code = code
        self.f = f
        self.right = right
        self.left = left


class Tree:
    def __init__(self, root=None):
        self.root = root

    def inorder(self):
        def inorder_(r, c):
            if r:
                inorder_(r.left, c)
                c.append((r.letter, r.code, r.f))
                inorder_(r.right, c)
            return c

        res = []
        return inorder_(self.root, res)

    def encoder(self):
        def encoder_(r, c):
            if r is None:
                return
            encoder_(r.right, c + "0")
            encoder_(r.left, c + "1")
            r.code = c

        root = self.root
        code = ""
        encoder_(root, code)


def encode(s):
    t = Tree()
    hq = []
    roots = []
    freq_map = {}
    for i in s:
        if i not in freq_map:
            freq_map[i] = 1
        else:
            freq_map[i] += 1

    code_map = {}
    for i in set(s):
        code_map[i] = ""

    freq = list(zip(freq_map.values(), freq_map.keys()))

    for i in freq:
        heapq.heappush(hq, i)

    while hq:
        fr1, l1 = heapq.heappop(hq)
        if t.root is not None:
            if l1 == t.root.letter:
                node1 = t.root
            else:
                node1 = Node(l1, f=fr1)
                for i in roots:
                    if node1.letter == i.letter:
                        node1 = i
                        break
        else:
            node1 = Node(l1, f=fr1)
            t.root = node1

        if hq:
            fr2, l2 = heapq.heappop(hq)
            if l2 == t.root.letter:
                node2 = t.root
            else:
                node2 = Node(l2, f=fr2)
                for i in roots:
                    if node2.letter == i.letter:
                        node2 = i
                        break
            new_node = Node(l1 + l2, f=fr1 + fr2, left=node2, right=node1)
            heapq.heappush(hq, (fr2 + fr1, l1 + l2))
            t.root = new_node
            roots.append(new_node)

    t.encoder()
    for i in t.inorder():
        if len(i[0]) == 1:
            code_map[i[0]] = i[1]

    code = ""
    for i in s:
        code += code_map[i]

    return code, code_map


def decode(s, d):
    rev_map = {}
    for k, v in d.items():
        rev_map[v] = k
    res = ""

    temp = ""
    for i in s:
        temp += i
        if temp in rev_map:
            res += rev_map[temp]
            temp = ""

    return res


print(encode("aabc"))
print(decode(*encode("aabc")))
