from set import Set
import unittest

if not hasattr(unittest.TestCase, 'assertCountEqual'):
    unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual

# Pair programmed with https://github.com/alishalabi/
class SetTest(unittest.TestCase):

    def test_init(self):
        s1 = Set(20)
        assert s1.max_size == 20
        assert s1.size == 0
        s2 = Set(4, ['cat', 'dog', 'fish'])
        assert s2.size == 3

    def test_contains(self):
        """
        return a boolean indicating whether element is in this set
        """
        s = Set(20)
        s.add('I')
        s.add('V')
        s.add('X')
        assert s.contains('I') == True
        assert s.contains('V') == True
        assert s.contains(0) == False
        assert s.contains(1) == False
        assert s.contains('X') == True

    def test_add(self):
        """
        add element to this set, if not present already
        """
        s = Set(3)
        assert s.keys() == []
        s.add('I')
        assert s.keys() == ['I']
        s.add('V')
        self.assertCountEqual(s.keys(), ['I', 'V'])  # Ignore item order
        s.add('X')
        self.assertCountEqual(s.keys(), ['I', 'V', 'X'])  # Ignore item order
        with self.assertRaises(Exception):
            s.add('A')  # Key does not exist

    def test_remove(self):
        """
        remove element from this set, if present, or else raise KeyError
        """
        s = Set(20)
        s.add('I')
        s.add('V')
        s.add('X')
        self.assertCountEqual(s.keys(), ['I', 'V', 'X'])
        s.remove('I')
        self.assertCountEqual(s.keys(), ['V', 'X'])

    def test_union(self):
        """
        return a new set that contains all items found in either this set and other_set
        """
        s1 = Set(20)
        s1.add('I')
        s1.add('V')
        s1.add('A')
        s2 = Set(20)
        s2.add('I')
        s2.add('V')
        union_s = s1.union(s2)
        self.assertCountEqual(union_s.keys(), ['I', 'V', 'A'])
        s2.add('B')
        union_s = s1.union(s2)
        self.assertCountEqual(union_s.keys(), ['I', 'V', 'A', 'B'])


    def test_intersection(self):
        """
        return a new set with items found in both this set and other_set
        """
        s1 = Set(20)
        s1.add('I')
        s1.add('V')
        s1.add('B')
        s2 = Set(20)
        s2.add('I')
        s2.add('V')
        intersection_s = s1.intersection(s2)
        self.assertCountEqual(intersection_s.keys(), ['I', 'V'])
        s2.add('B')
        intersection_s = s1.union(s2)
        self.assertCountEqual(intersection_s.keys(), ['I', 'V', 'B'])

    def test_difference(self):
        """
        return a new set that contains items appearing in this set but not other_set
        """
        s1 = Set(20)
        s1.add('I')
        s1.add('V')
        s1.add('A')
        s2 = Set(20)
        s2.add('I')
        s2.add('V')
        difference_s = s1.difference(s2)
        self.assertCountEqual(difference_s.keys(), ['A'])
        s2.add('B')
        difference_s = s1.difference(s2)
        self.assertCountEqual(difference_s.keys(), ['A'])

    def test_is_subset(self):
        """
        return a boolean indicating whether other_set is a subset of this set
        """
        s1 = Set(20)
        s1.add('I')
        s1.add('V')
        s1.add('A')
        s2 = Set(20)
        s2.add('I')
        s2.add('V')
        assert s1.is_subset(s2) == True
        s2.add('B')
        assert s1.is_subset(s2) == False

    # *----------------------------------------------*
    # Begin Stretch Challenge Tests

    def test_is_empty(self):
        """
        check if the buffer is empty
        """
        pass

    def test_is_full(self):
        """
        check if the buffer is full
        """
        pass

    def test_enqueue(self):
        """
        insert item at the back of the buffer
        """
        pass

    def test_dequeue(self):
        """
        remove and return the item at the front of the buffer
        """
        pass
