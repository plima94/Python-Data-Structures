"""
Python Data Structures - A Game-Based Approach
Stack class
Robin Andrews - https://compucademy.net/
"""


class Stack:
    # constructor
    def __init__(self):
        self.items = []

    # check if stack is empty
    def is_empty(self):
        # return len(self.items) == 0
        return not self.items

    # push item to the top of the stack
    def push(self, item):
        self.items.append(item)

    # remove items
    def pop(self):
        return self.items.pop()

    # returns the last item in the stack
    def peek(self):
        return self.items[-1]

    # returns the size of the stack
    def size(self):
        return len(self.items)

    # to string
    def __str__(self):
        return str(self.items)
