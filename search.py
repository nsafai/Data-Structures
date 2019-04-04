#!python
import math

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if value == item:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    if array[index] == item: # if value at current index matches item
        return index
    elif index + 1 < len(array): # if next index will still be in range
        return linear_search_recursive(array, item, index + 1) # try searching at next index
    else: # reached end of list without finding item
        return None 
        


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""

    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    if len(array) == 0: # list is empty
        return None
    
    accumulator = 0

    while len(array) > 0:
        middle_idx = int(len(array) / 2)
        middle_item = array[middle_idx]

        if middle_item == item:
            return middle_idx + accumulator
        if middle_item > item:
            return binary_search_recursive(array[:middle_idx], item, accumulator)
        elif middle_item < item:
            accumulator += len(array[:middle_idx]) + 1 # keeps track of how many sliced out of left side of array
            return binary_search_recursive(array[middle_idx+1:], item, accumulator)
    

def binary_search_recursive(array, item, accumulator = 0):
    if len(array) == 0: # list is empty
        return None

    middle_idx = int(len(array) / 2)
    middle_item = array[middle_idx]

    if middle_item == item:
        return middle_idx + accumulator
    if middle_item > item:
        return binary_search_recursive(array[:middle_idx], item, accumulator)
    elif middle_item < item:
        accumulator += len(array[:middle_idx]) + 1 # keeps track of how many sliced out of left side of array
        return binary_search_recursive(array[middle_idx+1:], item, accumulator)
