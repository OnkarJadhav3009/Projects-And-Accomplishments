import math
import random


class Node:
    def __init__(self, word):
        self.word = word
        self.next = None
        self.down = None


class LookUpSkipList:

    def __init__(self, words, probability):
        words.sort()
        self.head = None
        self.head = Node(words[0])
        temp = self.head
        self.levels = []
        self.c = []

        self.levels.append(self.head)
        self.c.append(1)
        for i in range(1, len(words)):
            self.c[-1] += 1
            new_node = Node(words[i])
            temp.next = new_node
            temp = temp.next

        self.levelCount = int(math.log2(self.c[0]))
        temp = self.levels[0]
        while temp:
            t = 0
            p = random.random()
            while p <= probability and self.levelCount > t >= 0 and self.c[t] <= \
                    self.c[0]:
                t += 1
                if t >= len(self.c):
                    self.c.append(1)
                    self.levels.append(Node(temp.word))
                else:
                    level_connector = self.levels[t]
                    while level_connector.next:
                        level_connector = level_connector.next
                    level_connector.next = Node(temp.word)
                    level_connector = level_connector.next
                    self.c[t] += 1
                p = random.random()
            temp = temp.next

        for i in range(len(self.levels) - 1):
            down_pointer = self.levels[i + 1]
            while down_pointer:
                temp = self.levels[i]
                while temp:
                    if down_pointer.word is temp.word and down_pointer.down is None:
                        down_pointer.down = temp
                    temp = temp.next
                down_pointer = down_pointer.next

    def print(self):
        for i in range(len(self.levels)):
            res = []
            temp = self.levels[i]
            while temp:
                res.append(temp.word)
                temp = temp.next
            print(res)

    def insert(self, word):
        self.c[0] += 1
        lvl = len(self.levels) - 1
        sentinel = self.levels[lvl]
        while sentinel.word > word and lvl > 0:
            lvl -= 1
            sentinel = self.levels[lvl]
        if lvl == 0:
            if sentinel.word > word:
                new_node = Node(word)
                new_node.next = self.head
                self.head = new_node
                self.levels[lvl] = new_node
            else:
                while sentinel.next and sentinel.next.word < word:
                    sentinel = sentinel.next
                new_node = Node(word)
                new_node.next = sentinel.next
                sentinel.next = new_node
        else:
            while sentinel.down:
                if sentinel.word > word:
                    sentinel = sentinel.down
                else:
                    if not sentinel.next:
                        sentinel = sentinel.down
                    else:
                        while sentinel.next and sentinel.next.word < word:
                            sentinel = sentinel.next
                        sentinel = sentinel.down
            if not sentinel.down:
                if not sentinel.next:
                    sentinel.next = Node(word)
                else:
                    while sentinel.next and sentinel.next.word < word:
                        sentinel = sentinel.next
                    if sentinel.next:
                        new_node = Node(word)
                        new_node.next = sentinel.next
                        sentinel.next = new_node
                    else:
                        sentinel.next = Node(word)

    def lookup_search(self, word):
        temp_traverse = self.head
        while temp_traverse:
            if temp_traverse.word == word:
                return True
            temp_traverse = temp_traverse.next
        print("ELEMENT NOT FOUND! INSERTING INTO SKIP LIST")
        self.insert(word)

    def delete(self, word):
        for i in range(len(self.levels)):
            sentinel = self.levels[i]
            prev = sentinel
            if sentinel.word == word:
                sentinel = sentinel.next
                self.levels[i] = sentinel
                self.c[i] -= 1
            elif sentinel:
                sentinel = sentinel.next
                while sentinel:
                    if sentinel.word == word:
                        prev.next = sentinel.next
                        self.c[i] -= 1
                        break
                    prev = prev.next
                    sentinel = sentinel.next
        for i in range(len(self.levels) - 1, -1, -1):
            if self.c[i] == 0:
                self.levels.pop()
                self.c.pop()


skip_list = LookUpSkipList(["iub", "usa", "there", "sort", "god"], 0.6)
print("Skip list : ")
skip_list.print()
print("---------------------------------------------------------------")
print("Insertion : ")
print("---------------------------------------------------------------")
skip_list.insert("abc")
skip_list.print()
print("---------------------------------------------------------------")
skip_list.insert("wasd")
skip_list.print()
print("---------------------------------------------------------------")
print("Search : ")
print("---------------------------------------------------------------")
print(skip_list.lookup_search("iub"))
skip_list.print()
print("---------------------------------------------------------------")
skip_list.lookup_search("zz")
skip_list.print()
print("---------------------------------------------------------------")
print("Deletion : ")
print("---------------------------------------------------------------")
skip_list.delete("zz")
skip_list.print()
print("---------------------------------------------------------------")
skip_list.delete("sort")
skip_list.print()
print("---------------------------------------------------------------")
