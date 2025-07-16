class Node:
    def __init__(self, data):
        self.data = data
        self.next: Node | None = None

class CircularLinkedList:
    def __init__(self):
        self.head: Node | None = None

    "PRINT ALL NODES (except head)"
    def print_linkedlist(self):
        if self.head is None:
            print("Empty LinkedList")
            return 
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
            if temp == self.head:
                print(f"{temp.data}[HEAD]")
                break
        print()
    
    "COUNT TOTAL NODES (except head)"
    def node_count(self):
        if self.head is None:
            return 0        
        temp, ctr = self.head, 0
        while temp:
            ctr+=1
            temp = temp.next
            if temp == self.head:
                break
        return ctr
    
    "INSERT NODES"
    """
    Insert at start:
    connect new node's next to self.head and last node which is pointing to head to newnode
    """
    def insert_node_at_start(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = Node(data)
            self.head.next = self.head
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        
        new_node.next = self.head # make new node's next point to head
        temp.next = new_node # make last node point to new node (completing the loop)
        self.head = new_node # make the newnode head

    """
    Insert at end:
    previous last node point to newnode, and newnode point to self.head
    """
    def insert_node_at_end(self, data):
        new_node = Node(data)

        if self.head is None: # no item in linked list
            new_node.next = new_node # as no item, so make the new_node point itself and head = newnode
            self.head = new_node
            return
        
        temp = self.head
        while temp.next!=self.head:
            temp = temp.next
        
        temp.next = new_node # last node points to new node
        new_node.next = self.head # new node's next point to head
    
    """
    Insert at any position
    go to pos-1, then do newnode.next=pos-1.next, pos-1.next = newnode
    """
    def insert_node_at_middle(self, data, position):
        if position <= 0:
            print("Invalid Position")
            return
        elif position == 1 or self.head is None:
            self.insert_node_at_start(data)
            return
        elif position == self.node_count() + 1:
            self.insert_node_at_end(data)
            return
        else:
            new_node = Node(data)
            i=1
            temp = self.head
            while i<position-1:
                temp = temp.next
                i+=1
            new_node.next = temp.next
            temp.next = new_node


    "DELETE NODES"
    """
    Delete start node
    """
    def delete_node_at_start(self):
        if self.head is None:
            print("Empty LinkedList")
            return
        temp = self.head
        while temp.next!=self.head:
            temp = temp.next
        temp.next = self.head.next # point to second item
        self.head = self.head.next # second item is the new head

    """
    Delete the last node
    """
    def delete_node_at_end(self):
        if self.head is None:
            print("Emplty LinkedList")
            return
        if self.head.next == self.head: # only 1 element
            self.head = None
            return
        temp = self.head
        while temp.next.next!=self.head: 
            # if the second last's next is self.head, then make the second last element new last element
            temp = temp.next
        temp.next = self.head
    
    """
    Delete the node at specified position
    """
    def delete_node_at_middle(self, position):
        if position <= 0:
            print("Invalid Position")
            return
        if position == 1:
            self.delete_node_at_start()
            return
        if position == self.node_count():
            self.delete_node_at_end()
            return
        temp, i = self.head, 1
        while i<position-1: # suppose u want to delete item at pos 3, so stop when u are at pos 2 and change links
            temp = temp.next
            i+=1
        # for 1 2 3 4 5 and pos=3, wee have to delete 3 and present temp is '2'
        # so, 2.next = (2.next).next = > 2.next = 3.next => 2.next = 4 thus removed item '3'
        temp.next = temp.next.next


    "SEARCH DATA FROM ALL NODES"
    "Linear Search"
    def search_linked_list_from_data_linear(self, data):
        temp = self.head
        i = 1
        while temp:
            if data == temp.data:
                return i
            temp = temp.next
            i+=1
            if temp == self.head:
                return -1
    
    "Binary Search: Sort the linkedlist then search, but here as I am doing call by reference (passing self and modifying the whole linkedlist) so the final linkedlist is sorted, to avoid this, better create a clone linkedlist function and use that clone/copy to find the item or just sort the linkedlist and find the item"
    "Binary Search"
    """
    Logic for binary search:
    i=0, j=len(a)-1
    while i<j: mid = (i+j)//2 if a[mid]==key found, 
    if key<a[mid] find from left, make j = mid-1,
    else if key>a[mid] find from right, make i = mid+1,
    after end of while loop return -1 not found
    """
    def search_linked_list_from_data_binary(self, data):
        self.sort_linked_list() # for binary sort always sort the data
        # after all these, I conclude that no we cannot do binary sort in circular linked list
        # as it will take O(n log n), thus go for linear search
        print("Cannot perform circular linked list as it is not optimal")
    
    """
    Clone LinkedList
    """
    def clone_linkedlist(self):
        new_lkList = CircularLinkedList()
        temp = self.head
        if temp is None: # if the original list is empty, return the empty linkedlist
            return new_lkList
        
        while True:
            new_lkList.insert_node_at_end(temp.data)
            temp = temp.next
            if temp == self.head:
                break
        return new_lkList


    "SORT LINKEDLIST"
    def sort_linked_list(self):
        if self.head is None:
            print("Empty LinkedList")
            return
        end = None # how many nodes are fully sorted, skip those nodes
        
        while True:
            swapped = 0
            curr = self.head # initialize i
            while curr.next!=end and curr.next!=self.head: # n-1-i
                print(f"Before swap curr = {curr.data}, curr.next = {curr.next.data}")
                if curr.data > curr.next.data:
                    curr.data, curr.next.data = curr.next.data, curr.data
                    swapped = 1
                    print(f"After swap curr = {curr.data}, curr.next = {curr.next.data}")
                curr = curr.next
                print(f"New curr = {curr.data}")
            end = curr
            print(f"Exited inner loop and end = {end.data}\n")
            if swapped == 0:
                print("All items are sorted ... Exiting program")
                break


if __name__ == "__main__":
    lk = CircularLinkedList()
    print("enter data for circular linked list: ")
    x = list(map(int, input().split()))

    lkList = [Node(i) for i in x]

    if lkList:
        lk.head = lkList[0]
        for j in range(len(lkList)-1):
            lkList[j].next = lkList[j+1]
        lkList[len(lkList)-1].next = lkList[0]
    
    # lk.print_linkedlist()
    # lk.insert_node_at_start("newnode at start")
    # lk.insert_node_at_end("newnode at end")
    # print(f"Total {lk.node_count()} Node(s) added")
    
    # lk.insert_node_at_middle(4,4) # try for 1 2 3
    # lk.insert_node_at_middle(5,4) # try for 1 2 3 4
    
    # lk.delete_node_at_start()
    # lk.delete_node_at_end()
    # lk.delete_node_at_middle(3) # try for 1 2 3 4 5    
        
    # lk.sort_linked_list()


    # LINEAR SEARCH IMPLEMENTATION
    """
    suppose list is 1 2 3 4, at pos1 we have 1, pos2 we have 2 and so on, linear search simply returns the position where we found the key, works on both sorted and unsorted data strcutures
    """
    # key = 4
    # result = lk.search_linked_list_from_data_linear(key)
    # if result!=-1:
    #     print(f"Found {key} at position {result}")
    # else:
    #     print(f"Item not found")


    # BINARY SEARCH IMPLEMENTATION
    copy = lk.clone_linkedlist() # apply binary sort to this
    copy.search_linked_list_from_data_binary(4)
    # cloning a linkedList, the "copy" is an object of CircularLinkedList class like "lk" 
    lk.print_linkedlist()

    """
    If u need to prove how they are linked
    print(lkList[0]) # <__main__.Node object at 0x0000021B51CAF250>
    print(lkList[len(lkList)-1].next) # <__main__.Node object at 0x0000021B51CAF250>
    """

"""
OUTPUT:
enter data for circular linked list: 
4 2 5 1 3 
4->2->5->1->3->4[HEAD] {before swap}

Before swap curr = 4, curr.next = 2
After swap curr = 2, curr.next = 4
New curr = 4
Before swap curr = 4, curr.next = 5
New curr = 5
Before swap curr = 5, curr.next = 1
After swap curr = 1, curr.next = 5
New curr = 5
Before swap curr = 5, curr.next = 3
After swap curr = 3, curr.next = 5
New curr = 5
Exited inner loop and end = 5

Before swap curr = 2, curr.next = 4
New curr = 4
Before swap curr = 4, curr.next = 1
After swap curr = 1, curr.next = 4
New curr = 4
Before swap curr = 4, curr.next = 3
After swap curr = 3, curr.next = 4
New curr = 4
Exited inner loop and end = 4

Before swap curr = 2, curr.next = 1
After swap curr = 1, curr.next = 2
New curr = 2
Before swap curr = 2, curr.next = 3
New curr = 3
Exited inner loop and end = 3

Before swap curr = 1, curr.next = 2
New curr = 2
Exited inner loop and end = 2

All items are sorted ... Exiting program
1->2->3->4->5->1[HEAD] {after swap}
"""