#!python
import sys # required for imports from a different folder
sys.path.append("..") # import any modules/folders present in parent folder
from linkedlist.linkedlist import LinkedList # from folder.filename import Class


# Implement LinkedQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class LinkedQueue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        # TODO: Check if empty

    def length(self):
        """Return the number of items in this queue."""
        # TODO: Count number of items

    def enqueue(self, item):
        """ Insert given item at back of queue
        Running time: O(???)"""
        pass

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        # TODO: Return front item, if any
    
    def deque(self):
        """Remove and return item at front of queue or raise ValueError if queue empty"""
        pass


# Implement ArrayQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class ArrayQueue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        # TODO: Check if empty

    def length(self):
        """Return the number of items in this queue."""
        # TODO: Count number of items
    
    def enqueue(self, item):
        """ Insert given item at back of queue
        Running time: O(???)"""
        pass

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        # TODO: Return front item, if any

    def deque(self):
        """Remove and return item at front of queue or raise ValueError if queue empty"""
        pass

# Implement LinkedQueue and ArrayQueue above, then change the assignment below
# to use each of your Queue implementations to verify they each pass all tests
Queue = LinkedQueue
# Queue = ArrayQueue
