# DOUBLY LINKED LIST IMPLEMENTATION (in your style)

class Node:
    def __init__(self, data):
        self.data = data
        self.prev: Node | None = None
        self.next: Node | None = None

class DoublyLinkedList:
    def __init__(self):
        self.head: Node | None = None

    "TRAVERSAL"
    def print_linkedlist(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

    "COUNT NODES"
    def node_count(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count

    "INSERT NODES"
    """
    Add item at end of linkedlist
    If list is empty, make new node as head
    Else traverse to last node and attach new_node
    """
    def insert_node_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    """
    Insert at beginning/start
    Update head to new node, and set pointers accordingly
    """
    def insert_node_at_start(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    """
    Insert at specific position
    Traverse to node before position, update pointers
    """
    def insert_node_at_middle(self, data, position):
        if position <= 0:
            print("Invalid position")
            return
        if position == 1:
            self.insert_node_at_start(data)
            return

        new_node = Node(data)
        temp = self.head
        i = 1
        while i < position - 1 and temp:
            temp = temp.next
            # suppose we have 10 <-> 20 <-> 30 <-> 40 <-> 50, and i have to add 25 between 2 & 3, i.e. position 3
            # then, go to the temp when it is 20 (done by temp = temp.next and  i<position-1)
            i += 1
        if temp is None:
            # if somehow temp is None, ofcourse we are out of list,  thus return error, else check below
            print("Position out of bounds")
            return
        new_node.next = temp.next # now, newnode (25)'s next points to temp(now 20)'s next i.e. 30, 25.next = 30, 25->30
        if temp.next: # now check if temp(20).next is not none
            temp.next.prev = new_node # if not none, then (20.next).prev which is 30.prev = 25
            # so we get 25 <-> 30 <-> ... completing the cycle of 25 and 30
        # now link the newnode 25 with 20 (30's old previous)
        temp.next = new_node # 20.next = 25, which is: 10 <-> 20 -> 25 <-> 30 <-> ... (single link)
        new_node.prev = temp # and finally 25.prev = 20 thus completing the cycle ... 20 <-> 25 <-> 30 ...

    "DELETE NODES"
    def delete_node_at_start(self):
        if self.head is None:
            print("Empty list")
            return
        if self.head.next is None: # linked list having 1 element
            self.head = None
            return
        self.head = self.head.next # suppose list is 1 <-> 2, then now head = 1.next which head = 2
        self.head.prev = None # and 2.prev = none, thus removing 1 from list

    def delete_node_at_end(self):
        if self.head is None:
            print("Empty list")
            return
        if self.head.next is None: # linked list having 1 element
            self.head = None
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.prev.next = None

    def delete_node_at_middle(self, position):
        if position <= 0:
            print("Invalid position")
            return
        if position == 1:
            self.delete_node_at_start()
            return

        temp = self.head
        i = 1
        while i < position and temp: # in deletion we use i<position
            temp = temp.next
            # suppose we have 10 <-> 20 <-> 30 <-> 40 <-> 50, and i have to delete element at position 3, i.e. 30
            # then, go to the temp when it is 30 (done by temp = temp.next and  i<position)
            i += 1
        if temp is None:
            print("Position out of bounds")
            return
        if temp.prev:
            # check if 30.prev exists, if yes then, (30.prev).next = 30.next
            # i.e. 20.next = 30.next => 20.next = 40
            temp.prev.next = temp.next
        if temp.next:
            # now check again if 30.next exists, if yes the (30.next).prev = 30.prev, 40.prev = 20
            temp.next.prev = temp.prev

    "SEARCH NODE"
    def search(self, data):
        temp = self.head
        while temp:
            if temp.data == data:
                return True
            temp = temp.next
        return False

    "SORT LINKED LIST"
    def sort_linked_list(self):
        curr = self.head
        if curr is None:
            print("Empty list")
            return
        while curr:
            index = curr.next
            while index:
                if curr.data > index.data:
                    curr.data, index.data = index.data, curr.data
                index = index.next
            curr = curr.next


if __name__ == '__main__':
    dll = DoublyLinkedList()
    print("Enter elements for doubly linked list:")
    x = list(map(int, input().split()))
    for i in x:
        dll.insert_node_at_end(i)
    dll.sort_linked_list()
    dll.print_linkedlist()
