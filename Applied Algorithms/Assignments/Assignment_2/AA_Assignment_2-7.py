class Node:
    def __init__(self, num, next=None):
        self.num = num
        self.next = next


class Linked_List():
    def __init__(self, head=None):
        self.head = head

    def Insert(self, element, position=None):
        new_node = Node(element)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            if position is None:
                while temp.next is not None:
                    temp = temp.next
                temp.next = new_node
            elif position > self.get_length():
                print("INVALID POSITION")
            else:
                c = 0
                while c != position - 1:
                    # if temp.next is None:
                    #     break
                    temp = temp.next
                    c += 1
                new_node.next = temp.next
                temp.next = new_node

    def delete(self, element):
        if self.head is None:
            print("No element in the list!")
        else:
            temp = self.head
            prev = None
            while temp is not None:
                if temp.num == element:
                    if prev is not None:
                        prev.next = temp.next
                    else:
                        temp = prev
                    break
                prev = temp
                temp = temp.next
            if temp is None:
                print("Element not in the list!")

    def Update(self, search_element, replace_element):
        temp = self.head
        while temp is not None:
            if temp.num == search_element:
                temp.num = replace_element
                break
            temp = temp.next
        if temp is None:
            print("Element not in the list!")

    def Search(self, element):
        temp = self.head
        while temp is not None:
            if temp.num == element:
                return True
            temp = temp.next
        return False

    def merge_linkedlists(self, ll):
        if ll is None:
            self.print()
        else:
            res = []
            temp1 = self.head
            temp2 = ll
            sorted_ll = Linked_List()
            while temp1 is not None and temp2 is not None:
                if temp1.num >= temp2.num:
                    sorted_ll.Insert(temp2.num)
                    sorted_ll.Insert(temp1.num)
                else:
                    sorted_ll.Insert(temp1.num)
                    sorted_ll.Insert(temp2.num)
                if temp1 is None:
                    temp2 = temp2.next
                elif temp2 is None:
                    temp1 = temp1.next
                else:
                    temp1 = temp1.next
                    temp2 = temp2.next
            sorted_ll.print()

    def get_length(self):
        length = 0
        temp = self.head
        while temp is not None:
            length += 1
            temp = temp.next
        return length

    def print(self):
        if self.head is None:
            print("Linked_List not created yet")
        temp = self.head
        print("______________LINK LIST___________________")
        while temp is not None:
            print(temp.num)
            temp = temp.next
        print("______________LINK LIST___________________")



# Insert
a = Linked_List()
a.Insert(1)
a.Insert(3)
a.Insert(5)
a.print()

# Insert in between
a.Insert(8,1)
a.print()

# Delete
a.Delete(8)
a.print()

# Update element
a.Update(5,7)
a.print()

# Element not in list
a.Update(6,7)
a.print()

# Search
a.Search(3)
a.Search(5)

# Merge Link List
b = Linked_List()
b.Insert(2)
b.Insert(4)
b.Insert(6)
b.print()

a.merge_linkedlists(b.head)

# Empty head Case
c = Linked_List()
a.merge_linkedlists(c.head)