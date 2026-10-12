class Node: # defining my node class
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self): # initializing linked list
        self.head = Node(-1) # dummy node
        self.tail = self.head
    
    def get(self, index: int) -> int:
        counter = 0
        current = self.head.next # pointer skipping dummy node
        while current: # while pointer is not none
            if counter == index:
                return current.data
            counter += 1
            current = current.next
        return -1 # index out of bounds

    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        current = self.head #pointer to dummy next location
        new_node.next = self.head.next #new node points to dummy's next location
        self.head.next = new_node #dummy points to new node
        
        #If List was empty on insertion
        if new_node.next is None:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        new_node = Node(val)
        self.tail.next = new_node
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        counter = 0
        current = self.head

        while current and counter < index:
            counter += 1
            current = current.next

        if current and current.next:
            if current.next.next is None:
                self.tail = current
            current.next = current.next.next
            return True
        return False

    def getValues(self) -> List[int]:
        array = []
        pointer = self.head.next
        while pointer:
            array.append(pointer.data)
            pointer = pointer.next
        
        return array