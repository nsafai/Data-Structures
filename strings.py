#!python
import time # for benchmarking

def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found.
    Time complexity: 
    Best: O(p) where p is # of chars in p, if pattern starts at index 0 in 'text'
    Worst: O(n) where n is # of chars in 'text', occurs if pattern not in text"""
    start_time = time.time()

    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    num_correct_letters = 0

    if len(pattern) == 0: # for pattern ''
        print('runtime was:', (time.time() - start_time))
        return 0 # all strings contain empty string
    elif len(pattern) > len(text): # pattern is too long to fit in text
        print('runtime was:', (time.time() - start_time))
        return None

    # for every letter in text while there's enough characters left to fit pattern
    for text_idx in range(len(text) - len(pattern) + 1):
        for pattern_idx, pattern_letter in enumerate(pattern): # look ahead for length of pattern to determine if there's a match
            if text[text_idx + pattern_idx] == pattern_letter: # if letters match
                num_correct_letters += 1
            else: # if letters do not match
                num_correct_letters = 0
                break

            if num_correct_letters >= len(pattern): # if we've found full pattern
                print('runtime was:', (time.time() - start_time))
                return text_idx # return index of starting letter inside text

    print('runtime was:', (time.time() - start_time))
    return None # reached end of word without finding a match
    # return text.index(pattern) if pattern in text else None # using built in python methods


def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text.
    Time complexity: 
    Best: O(p) where p is # of chars in p, if pattern starts at index 0 in 'text'
    Worst: O(n) where n is # of chars in 'text', occurs if pattern not in text"""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    return False if find_index(text, pattern) == None else True
    # return True if pattern in text else False # using built in python methods

def contains_recursive(text, pattern): # STRETCH CHALLENGE
    """Return a boolean indicating whether pattern occurs in text.
    Time complexity: 
    Best: O(p) where p is # of chars in p, if pattern starts at index 0 in 'text'
    Worst: O(n) where n is # of chars in 'text', occurs if pattern not in text"""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    if len(pattern) == 0:
        return True
    elif len(text) == 0:
        return False
    else:
        if text[0:len(pattern)] == pattern:
            return True
        else:
            return contains(text[1:], pattern) 

def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found.
    Time complexity: O(n - p) where n is # of characters in 'text' and p is length of the pattern. 
    Why? Because this algorithm needs to find ALL indexes where pattern starts
    so it needs to go through the entire text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    answer = []
    start_time = time.time()

    if pattern == '': # searching for empty string, return all results
        print('runtime was:', (time.time() - start_time))
        return list(range(len(text))) # there's a blank character at each index

    latest = find_index(text, pattern) # append latest index where pattern starts within text

    if latest == None:
        print('runtime was:', (time.time() - start_time))
        return answer

    while latest != None:
        answer.append(latest) # append latest index where pattern starts within text
        off_set = latest + 1 # off_set represents the next item to search == index after latest
        if find_index(text[off_set:], pattern) != None: # while there are more matches
            latest = find_index(text[off_set:], pattern) + off_set # update latest
        else: # no more indexes to find
            latest = None # update latest

    print('runtime was:', (time.time() - start_time))    
    return answer

def test_string_algorithms(text, pattern):
    start_time = time.time()
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))
    print('runtime for ALL tests was:', (time.time() - start_time))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        start_time = time.time()
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")
        print('runtime for basic tests was:', (time.time() - start_time))


if __name__ == '__main__':
    main()
