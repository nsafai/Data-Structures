#!python
import sys # required for imports from a different folder
sys.path.append("..") # import any modules/folders present in parent folder
from linkedlist.linkedlist import LinkedList # from folder.filename import Class

# Implement LinkedStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class LinkedStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        return True if self.list.size == 0 else False

    def length(self):
        """Return the number of items in this stack."""
        return self.list.size
    
    def push(self, item):
        """"Insert given item on top of stack
        Run time: O(??)"""
        self.list.prepend(item)
    
    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        head = self.list.head
        return None if head is None else head.data
    
    def pop(self):
        """Remove and return top item, if any, or raise ValueError if empty"""
        head = self.peek()
        self.list.delete(head)
        return head


# Implement ArrayStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class ArrayStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        return True if len(list) == 0 else len(list)

    def length(self):
        """Return the number of items in this stack."""
        # TODO: Count number of items
        pass
    
    def push(self, item):
        """"Insert given item on top of stack
        Run time: O(??)"""
        pass

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        # TODO: Return top item, if any
        pass
    
    def pop(self):
        """Remove and return top item, if any, or raise ValueError if empty"""
        pass


# Implement LinkedStack and ArrayStack above, then change the assignment below
# to use each of your Stack implementations to verify they each pass all tests
# Stack = LinkedStack
Stack = ArrayStack
