#!python

import string
# string.digits is '0123456789'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
NUM_CHARS = string.digits + string.ascii_lowercase # for base 36, the chars are [0-9a-z]

def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)

    digits = digits.lower() # convert all to lowercase so "A" is same as "a"
    answer = 0 # default value

    for power, digit in enumerate(reversed(digits)): # read from right side
        answer += NUM_CHARS.index(digit) * (base ** power)
        
    return answer
    # return int(digits, base)

def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    For example, turn a decimal (0-9) number '4' into binary (0-1) number '100'
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)

    answer = ""
    quotient = None
    
    while quotient is not 0:
        (quotient, remainder) = divmod(number, base) # divmod divides number by base and returns (quotient, remainder)
        answer += NUM_CHARS[remainder] # find index that corresponds with character r
        number = quotient # number get divided by base with each operation
    
    return answer[::-1] # returns a string in reverse order


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    
    num_base10 = decode(digits, base1)
    return encode(num_base10, base2)


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print(encode(23, 2))
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()
