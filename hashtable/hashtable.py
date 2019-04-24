#!python
import sys # required for imports from a different folder
sys.path.append("..") # import any modules/folders present in parent folder
from linkedlist.linkedlist import LinkedList # from folder.filename import Class

class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        self.buckets = [LinkedList() for _ in range(init_size)]
        self.size = 0  # Number of key-value entries

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        return hash(key) % len(self.buckets)

    def load_factor(self):
        """Return the load factor, the ratio of number of entries to buckets.
        Best and worst case running time: O(1) since self.size and self.buckets
        are both properties which are instantly accessible"""
        # Use float() so this is Python 2 compatible
        return float(self.size) / len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        Best and worst case running time: O(n) where n is number of buckets"""
        all_keys = []
        for bucket in self.buckets:
            for key, _ in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        Run time: O(n) where n is total # of items."""
        all_values = []
        for bucket in self.buckets:
            for _, value in bucket.items():
                all_values.append(value)
        return all_values

    def items(self):
        """Return a list of all entries (key-value pairs) in this hash table.
        Run-time is O(n), where n is the total # of items"""
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        Run-time is O(b) where b is # of buckets, because .size is O(1)"""
        return sum(bucket.size for bucket in self.buckets)

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        Run time:
        - O(1) best case, at head of LL
        - O(l) where l is the load factor.
        As size of hashtable increases, we will reach O(1), the # of elements
        per linkedlist will decrease"""
        # Find the bucket the given key belongs in
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        # Check if an entry with the given key exists in that bucket
        entry = bucket.find(lambda key_value: key_value[0] == key)
        return entry is not None  # True or False

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        Run time:
        - O(1) best case, at head of LL
        - O(l) where l is the load factor.
        As size of hashtable increases, we will reach O(1), the # of elements
        per linkedlist will decrease"""
        # Find the bucket the given key belongs in
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        # Find the entry with the given key in that bucket, if one exists
        entry = bucket.find(lambda key_value: key_value[0] == key)
        if entry is not None:  # Found
            # Return the given key's associated value
            assert isinstance(entry, tuple)
            assert len(entry) == 2
            return entry[1]
        else:  # Not found
            raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value=None):
        """Insert or update the given key with its associated value.
        Run time:
        - O(1) best case, at head of LL
        - O(l) where l is the load factor.
        As size of hashtable increases, we will reach O(1), the # of elements
        per linkedlist will decrease"""
        # Find the bucket the given key belongs in
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        # Find the entry with the given key in that bucket, if one exists
        # Check if an entry with the given key exists in that bucket
        entry = bucket.find(lambda key_value: key_value[0] == key)
        if entry is not None:  # Found
            # In this case, the given key's value is being updated
            # Remove the old key-value entry from the bucket first
            bucket.delete(entry)
        # Case: entry is not found, increase size of our hash table
        else:
            self.size += 1
        # Insert the new key-value entry into the bucket in either case
        bucket.append((key, value))
        # Check if the load factor exceeds a threshold such as 0.75
        if self.load_factor() > 0.75:
            # If so, resize the hash_table to reduce the load factor
            self._resize()

    def delete(self, key):
        """Delete the given key and its associated value, or raise KeyError.
        Run time:
        - O(1) best case, at head of LL
        - O(l) where l is the load factor.
        As size of hashtable increases, we will reach O(1), the # of elements
        per linkedlist will decrease"""
        # Find the bucket the given key belongs in
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        # Find the entry with the given key in that bucket, if one exists
        entry = bucket.find(lambda key_value: key_value[0] == key)
        if entry is not None:  # Found
            # Remove the key-value entry from the bucket
            bucket.delete(entry)
            self.size -= 1
        else:  # Not found
            raise KeyError('Key not found: {}'.format(key))

    def _resize(self, new_size=None):
        """Resize this hash table's buckets and rehash all key-value entries.
        Should be called automatically when load factor exceeds a threshold
        such as 0.75 after an insertion (when set is called with a new key).
        Best and worst case running time: O(n) where n is total # of items,
        because we need to rehash every item in the hash_table once the # of buckets changes
        Best and worst case space usage: O(2n) == O(n) where n is total # of items,
        because we need to rehash every item in the hash_table once the # of buckets changes"""
        # If unspecified, choose new size dynamically based on current size
        if new_size is None:
            new_size = len(self.buckets) * 2  # Double size
        # Option to reduce size if buckets are sparsely filled (low load factor)
        elif new_size is 0:
            new_size = len(self.buckets) / 2  # Half size
        # Get a list to temporarily hold all current key-value entries
        old_items = self.items()
        # Reset size property to 0, will be re-tallied in the set method
        self.size = 0
        # Create a new list of new_size total empty linked list buckets
        self.buckets = [LinkedList() for _ in range(new_size)]
        # Insert each key-value entry into the new list of buckets,
        # which will rehash them into a new bucket index based on the new size
        for key, value in old_items:
            self.set(key, value)


def test_hash_table():
    ht = HashTable(4)
    print('HashTable: ' + str(ht))

    print('Setting entries:')
    ht.set('I', 1)
    print('set(I, 1): ' + str(ht))
    ht.set('V', 5)
    print('set(V, 5): ' + str(ht))
    print('size: ' + str(ht.size))
    print('length: ' + str(ht.length()))
    print('buckets: ' + str(len(ht.buckets)))
    print('load_factor: ' + str(ht.load_factor()))
    ht.set('X', 10)
    print('set(X, 10): ' + str(ht))
    ht.set('L', 50)  # Should trigger resize
    print('set(L, 50): ' + str(ht))
    print('size: ' + str(ht.size))
    print('length: ' + str(ht.length()))
    print('buckets: ' + str(len(ht.buckets)))
    print('load_factor: ' + str(ht.load_factor()))

    print('Getting entries:')
    print('get(I): ' + str(ht.get('I')))
    print('get(V): ' + str(ht.get('V')))
    print('get(X): ' + str(ht.get('X')))
    print('get(L): ' + str(ht.get('L')))
    print('contains(X): ' + str(ht.contains('X')))
    print('contains(Z): ' + str(ht.contains('Z')))

    print('Deleting entries:')
    ht.delete('I')
    print('delete(I): ' + str(ht))
    ht.delete('V')
    print('delete(V): ' + str(ht))
    ht.delete('X')
    print('delete(X): ' + str(ht))
    ht.delete('L')
    print('delete(L): ' + str(ht))
    print('contains(X): ' + str(ht.contains('X')))
    print('size: ' + str(ht.size))
    print('length: ' + str(ht.length()))
    print('buckets: ' + str(len(ht.buckets)))
    print('load_factor: ' + str(ht.load_factor()))


if __name__ == '__main__':
    test_hash_table()
