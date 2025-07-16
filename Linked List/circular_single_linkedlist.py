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


    "SEARCH DATA FROM ALL NODES (try binary else go with linear)"
    def search_linked_list_from_data_linear(self, data):
        temp = self.head
        while temp:
            if data == temp.data:
                return True
            temp = temp.next
            if temp == self.head:
                return False


    "SORT LINKEDLIST"
    def sort_linked_list(self):
        if self.head is None:
            print("Empty LinkedList")
            return
        end = None # how many nodes are fully sorted, skip those nodes
        
        while True:
            swapped = 0
            curr = self.head
            while curr.next!=end and curr.next!=self.head: # n-1-i
                if curr.data > curr.next.data:
                    curr.data, curr.next.data = curr.next.data, curr.data
                    swapped = 1
                curr = curr.next
            end = curr
            if swapped == 0:
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
    
    lk.print_linkedlist()
    # lk.insert_node_at_start("newnode at start")
    # lk.insert_node_at_end("newnode at end")
    # print(f"Total {lk.node_count()} Node(s) added")
    
    # lk.insert_node_at_middle(4,4) # try for 1 2 3
    # lk.insert_node_at_middle(5,4) # try for 1 2 3 4
    
    # lk.delete_node_at_start()
    # lk.delete_node_at_end()
    # lk.delete_node_at_middle(3) # try for 1 2 3 4 5

    # print(lk.search_linked_list_from_data_linear(4))
    lk.sort_linked_list()
    lk.print_linkedlist()

    """
    If u need to prove how they are linked
    print(lkList[0]) # <__main__.Node object at 0x0000021B51CAF250>
    print(lkList[len(lkList)-1].next) # <__main__.Node object at 0x0000021B51CAF250>
    """