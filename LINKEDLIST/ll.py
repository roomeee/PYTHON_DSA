class Node:
    def __init__(self, value):
        # Node constructor to initialize data and next pointer
        self.data = value
        self.next = None


class LinkedList:
    def __init__(self):
        # LinkedList constructor to initialize head and size
        self.head = None  # Head of the linked list
        self.n = 0  # Size of the linked list

    def __len__(self):
        # Get the size of the linked list
        return self.n

    def __str__(self):
        # Convert the linked list to a string for printing
        current = self.head
        result = ''
        while current != None:
            result = result + str(current.data) + '->'
            current = current.next
        return result[:-2]  # Remove the trailing '->'

    def insert_head(self, value):
        # Insert a new node at the beginning of the linked list
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.n = self.n + 1

    def insert_tail(self, value):
        # Insert a new node at the end of the linked list
        new_node = Node(value)
        if self.head == None:
            # If the list is empty, set the new node as the head
            self.head = new_node
        else:
            # Traverse to the end and append the new node
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = new_node
        self.n = self.n + 1

    def insert_after(self, after, value):
        # Insert a new node after a specific value in the linked list
        new_node = Node(value)
        curr = self.head
        while curr != None:
            if curr.data == after:
                break
            curr = curr.next
        if curr != None:
            new_node.next = curr.next
            curr.next = new_node
            self.n = self.n + 1
        else:
            print("item not found")

    def delete_head(self):
        # Delete the node at the beginning of the linked list
        if self.head == None:
            print("empty list ")
        else:
            self.head = self.head.next
            self.n = self.n - 1

    def delete_tail(self):
        # Delete the node at the end of the linked list
        if self.head == None:
            print("empty list")
        else:
            curr = self.head
            if curr.next == None:
                # If there's only one element, call delete_head
                return self.delete_head()
            while curr.next != None:
                prev = curr
                curr = curr.next
            prev.next = None
            self.n = self.n - 1

    def remove(self, value):
        # Remove the first occurrence of a specific value in the linked list
        if self.head == None:
            print('Empty linked list')
        elif self.head.data == value:
            # If the value is in the head, call delete_head
            return self.delete_head()
        else:
            curr = self.head
            while curr.next != None:
                if curr.next.data == value:
                    break
                curr = curr.next
            if curr.next == None:
                print('Not found')
            else:
                curr.next = curr.next.next
                self.n = self.n - 1

    def __getitem__(self, index):
        # Get the value at a specific index in the linked list
        curr = self.head
        pos = 0
        while curr != None:
            if pos == index:
                return curr.data
            curr = curr.next
            pos = pos + 1

        return 'index error'


L = LinkedList()
L.insert_head(1)
L.insert_head(2)
L.insert_head(3)
L.insert_tail(45)
L.insert_after(45, 7)
print(L)
