#!python
import sys # required for imports from a different folder
sys.path.append("..") # import any modules/folders present in parent folder
from hashtable.hashtable import HashTable # from folder.filename import Class

# Pair programmed with https://github.com/alishalabi/
class Set(HashTable):
    def __init__(self, max_size=8):
        """
        initialize a new circular buffer that can store at most max_size items
        """
        HashTable.__init__(self)
        self.max_size = max_size

    # Inheriting contains from superclass
    # def contains(element):
    #     """
    #     return a boolean indicating whether element is in this set
    #     """
    #     return element is in self

    def add(self, element):
        """
        add element to this set, if not present already
        """
        if self.size < self.max_size:
            self.set(element)
        else:
            raise Exception('Set is full, could not add: {}'.format(element))

    def remove(self, element):
        """
        remove element from this set, if present, or else raise KeyError
        """
        self.delete(element)

    def union(self, other_set):
        """
        return a new set that contains all items found in either this set and other_set
        """
        union_set = Set()
        # Append each element in first HT
        for element in self.keys():
            union_set.add(element)
        # Append each element in second HT (duplicates resolved in HT method)
        for element in other_set.keys():
            union_set.add(element)
        return union_set

    def intersection(self, other_set):
        """
        return a new set with items found in both this set and other_set
        """
        intersection_set = Set()
        for element in self.keys():
            if element in other_set.keys():
                intersection_set.set(element)
        return intersection_set

    def difference(self, other_set):
        """
        return a new set that contains items appearing in this set but not other_set
        """
        difference_set = Set()
        for element in self.keys():
            if element not in other_set.keys():
                difference_set.set(element)
        return difference_set

    def is_subset(self, other_set):
        """
        return a boolean indicating whether other_set is a subset of this set
        """
        for element in other_set.keys():
            if element not in self.keys():
                return False
        return True

    # *----------------------------------------------*
    # Begin Stretch Challenge Tests
    def is_empty(self):
        """
        check if the buffer is empty
        """
        pass

    def is_full(self):
        """
        check if the buffer is full
        """
        pass

    def enqueue(self, item):
        """
        insert item at the back of the buffer
        TODO: Time complexity
        """
        pass

    def dequeue(self):
        """
        remove and return the item at the front of the buffer
        TODO: Time complexity
        """
        pass