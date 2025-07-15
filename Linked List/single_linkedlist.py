class Node:
    def __init__(self, data):
        self.data = data
        self.next: Node | None = None

class LinkedList:
    def __init__(self):
        self.head: Node | None = None
        # variable : datatype1 | (or) datatype = initial value
        # wrote like this as pylance (VS code's intellisense had issues)

    "TRAVERSAL OF LINKEDLIST"
    def print_linkedlist(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print()

    "COUNT NODES"
    def node_count(self):
        temp = self.head
        count=0
        while temp:
            count+=1
            temp = temp.next
        return count

    "INSERT NODES"
    """
    Add item at end of linkedlist
    logic: take input and create a new node, (let newnode) traverse through the total linkedlist and find the node before than the node whose next is null(let temp)), now temp->next = newnode, and newnode->next is already None
    """
    def insert_node_at_end(self, data):
        new_node = Node(data)

        if self.head == None:
            # incase there is node in linkedlist
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            """
            do this until temp.next is not none, 
            like this when temp is none and loop breaks we have the temp value which is not none
            """
            temp = temp.next
        temp.next = new_node
    
    """
    Insert at beginning/ start (ts('beginning') too tough to write)
    Change next of new node to point to head, then change head to point to recently created node
    """
    def insert_node_at_start(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head = new_node

    """
    Insert data at user defined position
    Traverse to node just before the required position of new node, then change next pointers to include new node in between
    """
    def insert_node_at_middle(self, data, position): # position starts from 1 to n
        if position == 1:
            self.insert_node_at_start(data)
            return
        elif position <= 0:
            print("Invalid position ... position starts from 1")
            return
        
        new_node = Node(data)
        temp = self.head
        if temp:
            i=1
            while(i<position-1):
                if temp is None:
                    print("Position out of bound")
                    return
                temp = temp.next
                i+=1
            if temp is None:
                print("Position out of bound")
                return
            new_node.next = temp.next
            temp.next = new_node
        else:
            self.insert_node_at_start(data)
    
    "DELETE NODES"
    """
    Delete node at end of lined list
    Traverse to second last element, change its next pointer to null
    """
    def delete_node_at_end(self):
        if self.head is None:
            print("Empty LinkedList")
            return
        
        # if linked list has only 1 node
        if self.head.next is None:
            self.head = None
            return

        temp = self.head
        while temp.next is not None and temp.next.next is not None:
            # when it reaches the 2nd last element, and checks that it's next is present but after that there is nothing it deleted the node after it (i.e. the last node)
            temp = temp.next
        temp.next = None

    """
    DELETE NODE AT START
    Point head to the second node
    """
    def delete_node_at_start(self):
        if self.head is not None:
            self.head = self.head.next
        else:
            print("Empty LinkedList")

    """
    DELETE NODE FROM MIDDLE
    Traverse to the node just before the one you want to delete, and update its next pointer to skip over the target node by linking it to the target node's next
    """
    def delete_node_at_middle(self, postion): # position starts from 1 to n
        if postion == 1:
            self.delete_node_at_start()
            return
        elif postion <= 0:
            print("Invalid position ... position starts from 1")
            return
        
        if self.head is None:
            print("Empty LinkedList")
            return
        
        temp = self.head
        i = 1

        while(i<postion-1):
            if temp is None or temp.next is None:
                print("Poisiton out of bounds")
                return
            temp = temp.next
            i+=1
        
        if temp.next is None:
            print("Poisiton out of bounds")
            return

        # delete node
        temp.next = temp.next.next
     

    "SEARCH LINKEDLIST"
    def search_linked_list_from_data(self, data):
        if self.head is None:
            print("Empty LinkedList")
            return False
        
        temp = self.head
        while temp:
            if temp.data == data:
                return True
            temp = temp.next
        return False


    "SORT LINKEDLIST"
    def sort_linked_list(self):
        pass
    


if __name__ == "__main__":
    """
        --- create nodes ---
            lnklist = LinkedList() # create linkedlist object
            lnklist.head = Node(1) # assign the first node as linkedlist's head
            second = Node(2) # and create other nodes, which will be linked later on
            third = Node(3)

            lnklist.head.next = second # now the next of linedlist's head is the second
            second.next = third # and the next of second node is third
    """
    
    lk = LinkedList()
    print("data point entry for linked list")
    x = list(map(int, input().split()))

    lkData = [Node(i) for i in x]

    if lkData:
        lk.head = lkData[0]
        # assign next values to each except the first node
        for j in range(len(lkData)-1):
            lkData[j].next = lkData[j+1]
    
    # lk.insert_node_at_start(0)
    # lk.insert_node_at_end(100)
    # lk.print_linkedlist()
    # lk.insert_node_at_middle(6, 1)
    # lk.print_linkedlist()

    # print(lk.node_count())

    # lk.delete_node_at_start()
    # lk.delete_node_at_end()
    # lk.print_linkedlist()
    # lk.delete_node_at_middle(3)
    # lk.print_linkedlist()

    ipt = int(input("data to search ?"))
    result = lk.search_linked_list_from_data(ipt)
    if result:
        print("found")
    else:
        print("not found")