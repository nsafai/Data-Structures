#!python

import string
import re
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
letters = string.ascii_letters

def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    # return is_palindrome_iterative(text)
    return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    if len(text) == 0: # if text is an empty string ''
        return True

    median_idx = (len(text) // 2) + 1 # get midpoint of word
    text = re.sub(r'\W+', '', text).lower() # removes spaces, punctuation & capitalization

    for i in range(median_idx): # for every index until midpoint of word
        if text[i] == text[-(i + 1)]: # if 1st letter same as last
            pass
        else:
            return False
    return True


def is_palindrome_recursive(text, left=None, right=None):
    
    if left == None: # only true first time this function gets called
        text = re.sub(r'\W+', '', text).lower()
        left = 0
        right = len(text) - 1
    
    if left >= right: # exit condition --> reached middle of word
        return True
    
    if text[left] == text[right]: # letter at left index is same as right
        left += 1
        right -= 1
        return is_palindrome_recursive(text, left, right)
    else:
        return False

def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
