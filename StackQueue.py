import sys


class MyStack:

    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def peek(self):
        if len(self._data) == 0:
            raise IndexError("Stack is empty")
        return self._data[len(self._data)-1]

    def pop(self):
        return self._data.pop()

    def __len__(self):
        return len(self._data)

    def get_size(self):
        return sys.getsizeof(self._data)


class CircularQueue:
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * CircularQueue.DEFAULT_CAPACITY
        self._number_of_items = 0
        self._front_index = 0

    def __len__(self):
        return self._number_of_items

    def is_empty(self):
        return self._number_of_items == 0

    def first(self):
        if self.is_empty():
            raise IndexError("Empty Queue")
        return self._data[self._front_index]

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Empty Queue")
        value = self._data[self._front_index]
        self._data[self._front_index] = None
        self._front_index = (self._front_index+1) % len(self._data)
        self._number_of_items -= 1
        return value

    def enqueue(self, item):
        if self._number_of_items == len(self._data):
            self._resize(len(self._data)*2)
        next_available_index = \
            (self._front_index + self._number_of_items) \
            % len(self._data)
        self._data[next_available_index] = item
        self._number_of_items += 1

    def _resize(self, capacity):
        old_data = self._data
        self._data = [None]*capacity
        current_index = self._front_index
        for index in range(0, len(old_data)):
            self._data[index] = old_data[current_index]
            current_index = (current_index+1) % len(old_data)
        self._front_index = 0

    def get_size(self):
        return sys.getsizeof(self._data)
