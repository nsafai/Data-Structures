#!python

def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    num_correct_letters = 0

    if len(pattern) == 0: # for pattern ''
        return 0 # all strings contain empty string

    for text_idx, _ in enumerate(text): # for every letter in text
        for pattern_idx, pattern_letter in enumerate(pattern): # look ahead for length of pattern to determine if there's a match
            if text[text_idx + pattern_idx] == pattern_letter: # if letters match
                num_correct_letters += 1
            else: # if letters do not match
                num_correct_letters = 0
                break

            if num_correct_letters >= len(pattern): # if we've found full pattern
                return text_idx # return index of starting letter inside text

    return None # reached end of word without finding a match

    # return text.index(pattern) if pattern in text else None # using built in python methods


def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    
    return False if find_index(text, pattern) == None else True
    # return True if pattern in text else False # using built in python methods


def find_all_indexes(text, pattern, answer=[]):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    latest_index = answer[-1]

    while find_index(text, pattern[latest_index:]) != None:
        answer.append(find_index(text, pattern[latest_index:]))
    
    if answer == []:
        return None
    else:
        return answer


def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()
