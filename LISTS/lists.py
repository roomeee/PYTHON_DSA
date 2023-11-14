import ctypes


class MyList:
    def __init__(self):
        # Constructor initializes the MyList object with default values.
        self.size = 1  # maximum items to be stored
        self.n = 0  # items stored
        # Create a c type array with size
        self.A = self.__make_array(self.size)

    def __len__(self):
        # Returns the number of items currently stored in the list.
        return self.n

    def __str__(self):
        # Returns a string representation of the list.
        result = ''
        for i in range(self.n):
            result = result + str(self.A[i]) + ','
        return '[' + result[:-1] + ']'

    def __delitem__(self, pos):
        # Deletes an item at the specified position in the list.
        if 0 <= pos < self.n:
            for i in range(pos, self.n - 1):
                self.A[i] = self.A[i + 1]
            self.n = self.n - 1

    def __getitem__(self, index):
        # Returns the item at the specified index in the list.
        if 0 <= index < self.n:
            return self.A[index]
        else:
            return 'Index out of range'

    def __make_array(self, capacity):
        # Creates a c type array with the specified capacity.
        # This array is a referential array to store Python objects.
        return (capacity * ctypes.py_object)()

    def append(self, item):
        # Appends an item to the end of the list.
        if self.n == self.size:
            self.__resize(self.size * 2)
        self.A[self.n] = item
        self.n = self.n + 1

    def extend(self, list_b):
        # Extends the list by appending items from another list.
        for items in list_b:
            self.append(items)

    def __resize(self, new_capacity):
        # Resizes the array to the specified new capacity.
        # This is done when the list is full to accommodate more items.
        B = self.__make_array(new_capacity)
        self.size = new_capacity
        for i in range(self.n):
            B[i] = self.A[i]
        self.A = B

    def pop(self):
        # Removes and returns the last item from the list.
        if self.n == 0:
            return 'Empty list'
        print(self.A[self.n - 1])
        self.n = self.n - 1

    def clear(self):
        # Clears the list by resetting the item count and size.
        self.n = 0
        self.size = 1

    def find(self, item):
        # Finds the index of the first occurrence of the specified item.
        # Returns an error message if the item is not in the list.
        for i in range(self.n):
            if self.A[i] == item:
                return i
        return 'ValueError not in list'

    def insert(self, pos, item):
        # Inserts an item at the specified position in the list.
        if self.n == self.size:
            self.__resize(self.size * 2)
        for i in range(self.n, pos, -1):
            self.A[i] = self.A[i - 1]
        self.A[pos] = item
        self.n = self.n + 1

    def remove(self, item):
        # Removes the first occurrence of the specified item in the list.
        # Returns an error message if the item is not in the list.
        pos = self.find(item)
        if type(pos) == int:
            self.__delitem__(pos)
        else:
            return pos

    # def sort(self):
    #     # Sorts the list in ascending order using Python's built-in sorted function.
    #     self.A[:self.n] = sorted(self.A[:self.n])
    #
    # def min(self):
    #     # Returns the minimum value in the list using Python's built-in min function.
    #     if self.n == 0:
    #         return 'Empty list'
    #     return min(self.A[:self.n])

    def max(self):
        # Returns the maximum value in the list using Python's built-in max function.
        if self.n == 0:
            return 'Empty list'
        max_val = self.A[0]
        for i in range(1, self.n):
            if self.A[i] > max_val:
                max_val = self.A[i]
        return max_val

    def sort(self):
        # Sorts the list in ascending order without using the built-in sorted function.
        for i in range(self.n - 1):
            for j in range(0, self.n - i - 1):
                if self.A[j] > self.A[j + 1]:
                    self.A[j], self.A[j + 1] = self.A[j + 1], self.A[j]

    def min(self):
        # Returns the minimum value in the list without using the built-in min function.
        if self.n == 0:
            return 'Empty list'
        min_val = self.A[0]
        for i in range(1, self.n):
            if self.A[i] < min_val:
                min_val = self.A[i]
        return min_val

    def sum(self):
        # Returns the sum of all elements in the list using Python's built-in sum function.
        result_Sum = 0
        for i in range(self.n):
            result_Sum += self.A[i]
        return result_Sum


# # Example usage:
# L = MyList()
# L.append(1)
# L.append(100)
# L.append(3.4)
# L.append(21)
# print(len(L))
# print(L)
#
# # Sorting the list
# L.sort()
# print("Sorted list:", L)
#
# # Adding more elements and extending the list
# List_b = [32, 86]
# L.extend(List_b)
# print("Extended list:", L)
#
# # Displaying the minimum, maximum, and sum of the elements in the list
# print("Minimum:", L.min())
# print("Maximum:", L.max())
# print("Sum:", L.sum())
