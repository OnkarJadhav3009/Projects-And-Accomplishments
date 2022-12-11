class Node:

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def get_height(r):
    if r is None:
        return 0
    else:
        lft = get_height(r.left)
        rgt = get_height(r.right)
        return 1 + max(lft, rgt)


class BST:

    def __init__(self, root):
        self.root = root

    def __contains__(self, data):
        r = self.root
        while r is not None:
            if data < r.data:
                r = r.left
            elif data > r.data:
                r = r.right
            else:
                return True
        return False

    def insert(self, data=None):

        root = self.root

        while root is not None:
            prev = root
            if data is None:
                print("DATA IS NULL!!!")
                break
            if data in self:
                print(data, "ALREADY IN THE TREE!!!")
                break
            if data > root.data:
                root = root.right
                if root is None:
                    prev.right = Node(data)
                    break
            elif data < root.data:
                root = root.left
                if root is None:
                    prev.left = Node(data)
                    break

    def delete(self, data):

        r = self.root

        if data not in self:
            print("DATA NOT IN THE TREE")
        else:
            prev = r
            while r is not None:
                if r.data == data:
                    break
                if data < r.data:
                    prev = r
                    r = r.left
                elif data > r.data:
                    prev = r
                    r = r.right

            # print(prev.data, r.data)

            if r.right is None and r.left is None:
                if prev == r:
                    self.root = None
                if prev.right == r:
                    prev.right = None
                elif prev.left == r:
                    prev.left = None
            elif r.right and r.left is None:
                if prev == r:
                    self.root = prev.right
                if prev.right == r:
                    prev.right = r.right
                elif prev.left == r:
                    prev.left = r.right
            elif r.left and r.right is None:
                if prev == r:
                    self.root = prev.left
                if prev.right == r:
                    prev.right = r.left
                elif prev.left == r:
                    prev.left = r.left
            elif r.left and r.right:
                temp = r.right
                p = r
                while temp.left is not None:
                    p = temp
                    temp = temp.left
                temp.data, r.data = r.data, temp.data
                if p == r:
                    p.right = None
                else:
                    p.left = None

    def preorder(self):
        def preorder_(r, c):
            if r:
                c.append(r.data)
                preorder_(r.left, c)
                preorder_(r.right, c)
            return c

        res = []
        return preorder_(self.root, res)

    def postorder(self):
        def postorder_(r, c):
            if r:
                postorder_(r.left, c)
                postorder_(r.right, c)
                c.append(r.data)
            return c

        res = []
        return postorder_(self.root, res)

    def inorder(self):
        def inorder_(r, c):
            if r:
                inorder_(r.left, c)
                c.append(r.data)
                inorder_(r.right, c)
            return c

        res = []
        return inorder_(self.root, res)

    def level_order(self):
        def count_element(r, c_):
            if r:
                count_element(r.left, c_)
                c_.append(r)
                count_element(r.right, c_)

        def level_order_(r, l_, c_):
            if r is None:
                return
            elif l_ == 0:
                c_.append(r.data)
            else:
                level_order_(r.left, l_ - 1, c_)
                level_order_(r.right, l_ - 1, c_)
            return res

        lvl = 0
        c = []
        count = 0
        res = []
        count_element(self.root, c)
        while count < len(c):
            res = level_order_(self.root, lvl, res)
            lvl += 1
            count += 1
        return res

    def diameter(self):
        def get_diameter(node):
            max_ = 0
            lft = get_height(node.left)
            rht = get_height(node.right)
            if node.left and node.right:
                return lft + rht
            elif node.left and not node.right:
                return lft
            elif node.right and not node.left:
                return rht
            return 0

        def traverse(r_, c):
            if r_ is None:
                return
            else:
                # print(r_.data, get_diameter(r_))
                if c < get_diameter(r_):
                    c = get_diameter(r_)
                traverse(r_.right, c)
                traverse(r_.left, c)
            return c

        r = self.root
        return traverse(r, 0)

    def heights(self):
        root = self.root
        return get_height(root)

    def max(self):
        temp = self.root
        while temp.right is not None:
            temp = temp.right
        return temp.data


# Create root
t = BST(Node(10))
# # Insertion
t.insert(15)
t.insert(12)
# t.insert(18)
t.insert(16)
t.insert(9)
# Null case
t.insert()
t.insert(11)
t.insert(10)

# skew
# t.insert(12)
# t.insert(15)
# t.insert(16)

# Inorder traversal
# contains__ dunder method
print("<------------------------------------------------------------->\nCONTAINS DUNDER METHOD:")
print("12 in t?: ", 12 in t)
print("1 in t?: ", 1 in t, end=" ")
print("\n<------------------------------------------------------------->")
# get max num of the tree
print("<------------------------------------------------------------->\nMAXIMUM OF THE TREE:")
print(t.max())
print("\n<------------------------------------------------------------->")
print("<------------------------------------------------------------->\nIN ORDER:")
print(t.inorder())
print("\n<------------------------------------------------------------->")
print("<------------------------------------------------------------->\nPRE ORDER:")
print(t.preorder())
print("\n<------------------------------------------------------------->")
print("<------------------------------------------------------------->\nPOST ORDER:")
print(t.postorder())
print("\n<------------------------------------------------------------->")
print("<------------------------------------------------------------->\nLEVEL ORDER:")
print(t.level_order())
print("\n<------------------------------------------------------------->")
print("<------------------------------------------------------------->\nMAX HEIGHT:")
print(t.heights())
print("\n<------------------------------------------------------------->")
print("<------------------------------------------------------------->\nDIAMETER:")
print(t.diameter())
print("\n<------------------------------------------------------------->")
print("<------------------------------------------------------------->\nDELETE:")
print(t.level_order())
t.delete(10)
print("AFTER DELETION")
print(t.level_order())
print("\n<------------------------------------------------------------->")
