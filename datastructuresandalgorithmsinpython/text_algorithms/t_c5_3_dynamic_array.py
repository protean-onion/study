#!/usr/bin/python3

import ctypes                                # provides low-level arrays

class DynamicArray:
    """A dynamic array class akin to a simplified Python list."""

    def __init__(self):
        """Create an empty array."""
        self._n = 0                          # count actual elements
        self._capacity = 1                   # default array capacity
        self._A = self._make_array(self._capacity)  # low-level array

    def __len__(self):
        """Return number of elements stored in the array."""
        return self._n

    def __getitem__(self, k):
        """Return element at index k."""
        if not self._n * -1 <= k < self._n:
            raise IndexError('invalid index')
        if k < 0:
            return self._A[self._n + k]
        else:
            return self._A[k]                    # retrieve from array

    def append(self, obj):
        """Add object to end of the array."""
        if self._n == self._capacity:        # not enough room
            self._resize(2 * self._capacity) # so double capacity
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):                    # nonpublic utitity
        """Resize internal array to capacity c."""
        B = self._make_array(c)              # new (bigger) array
        for k in range(self._n):             # for each existing value
            B[k] = self._A[k]
        self._A = B                          # use the bigger array
        self._capacity = c

    def _make_array(self, c):                # nonpublic utitity
        """Return new array with capacity c."""
        return (c * ctypes.py_object)()

    def my_add_element(self, element, index): # Let's do this. The first function I wrote returned an almost correct object. I was shocked. How could it be that easy? How could I have done it?
        new_size = self._n + 1
        if new_size > self._capacity:
            self._capacity *= 2

        B = self._make_array(self._capacity) # Ughhh that's why. I had `self._capacity` as the argument here.
    
        for i in range(index):
            B[i] = self._A[i]
        B[index] = element
        for i in range(index + 1, new_size):
            B[i] = self._A[i - 1]
        
        self._A = self._make_array(self._capacity)
        for i in range(new_size):
            self._A[i] = B[i]
        self._capacity = self._capacity
        self._n = new_size
    
    def my_replace_element(self, target, element):
        for i in range(self._n):
            if self._A[i] == target:
                self._A[i] = element
        
    def intersperse(self, element, begin, step):
        for i in range(begin, self._n, step):
            self._A[i] = element

    def insert(self, k, value):
        """Insert value at index k, shifting subsequent values rightward."""
        # (for simplicity, we assume 0 <= k <= n in this verion)
        if self._n == self._capacity:            # not enough room
            final = self._A[self._n - 1]
            for j in range(self._n - 1, k, -1):
                self._A[j] = self._A[j - 1]
            self._resize(2 * self._capacity)     # so double capacity
            self._A[self._n] = final
        else:
            for j in range(self._n, k, -1):
                self._A[j] = self._A[j - 1]
        self._A[k] = value                       # store newest element
        self._n += 1

    def remove_element(self, value):
        for i in range(self._n):
            if self._A[i] == value:
                for j in range(i, self._n - 1):
                    self._A[j] = self._A[j + 1]
                self._A[self._n - 1] = ctypes.py_object()
                self._n -= 1

def main():
    a = DynamicArray()
    
    for i in range(10):
        a.append(i)

    # a.my_add_element(100, 5)
    a.remove_element(5)
    for i in range(a._n):
        print(a[i])

if __name__ == "__main__":
    main()