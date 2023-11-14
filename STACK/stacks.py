from LISTS.lists import MyList


class Stack:
    def __init__(self):
        # Create an instance of the MyList class to use its methods for stack operations.
        self.my_list = MyList()

    def is_empty(self):
        # Returns True if the stack is empty, otherwise False.
        return len(self.my_list) == 0

    def push(self, item):
        # Adds an item to the top of the stack.
        self.my_list.append(item)

    def pop(self):
        # Removes and returns the item from the top of the stack.
        if self.is_empty():
            return 'Stack is empty'
        popped_item = self.my_list[self.my_list.__len__() - 1]
        self.my_list.__delitem__(self.my_list.__len__() - 1)
        return popped_item

    def peek(self):
        # Returns the item from the top of the stack without removing it.
        if self.is_empty():
            return 'Stack is empty'
        return self.my_list[self.my_list.__len__() - 1]

    def size(self):
        # Returns the number of items in the stack.
        return len(self.my_list)

# Example usage:
stack = Stack()

# Pushing elements onto the stack
stack.push(5)
stack.push('hello')
stack.push(True)

# Displaying the stack
print("Stack:", stack.my_list)

# Popping an element from the stack
popped_item = stack.pop()
print("Popped item:", popped_item)

# Displaying the updated stack
print("Updated Stack:", stack.my_list)

# Peeking at the top element of the stack
top_item = stack.peek()
print("Top item:", top_item)

# Displaying the size of the stack
print("Size of the stack:", stack.size())
