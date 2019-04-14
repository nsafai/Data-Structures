#!python

import string
import re
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
LETTERS = set(string.ascii_letters)

def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    # return is_palindrome_iterative(text)
    return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    left = 0 # starts as first letter
    right = len(text) - 1 # starts as last letter

    while left < right: # until we reach middle of word and left = right

        if text[left] not in LETTERS: # if left is not a letter
            left += 1 # skip that character
        if text[right] not in LETTERS: # if right not a letter
            right -= 1 # skip that character

        if text[left] in LETTERS and text[right] in LETTERS:
            if text[left] == text[right]: # if letters are same w/o changing case
                # keep shrinking window
                left += 1
                right -= 1
            elif text[left].lower() == text[right].lower(): # if letters are same in lowercase
                # keep shrinking window
                left += 1
                right -= 1
            else: # if letters are different
                return False

    return True # reached end of word


def is_palindrome_recursive(text, left=0, right=None):
    
    if right == None: # only true first time this function gets called
        right = len(text) - 1
    
    if left > right: # reached middle of word, b/c when left == right, it is the same letter
        return True

    if text[left] not in LETTERS:
        return is_palindrome_recursive(text, left + 1, right) # skip text[left] if not a letter
    if text[right] not in LETTERS:
        return is_palindrome_recursive(text, left, right - 1) # skip text[right] if not a letter
    
    if text[left] == text[right]: # letters are same w/o changing case
        return is_palindrome_recursive(text, left + 1, right - 1)
    elif text[left].lower() == text[right].lower(): # if letters are same in lowercase
        return is_palindrome_recursive(text, left + 1, right - 1)
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
