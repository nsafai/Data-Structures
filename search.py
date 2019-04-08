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
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    left = 0
    right = len(array) - 1

    while left <= right:
        median_idx = (left + right) // 2
        median_item = array[median_idx]

        if median_item == item:
            return median_idx
        elif median_item <= item:
            # chop off anything smaller than median_item
            left = median_idx + 1
        elif median_item >= item:
            # chop off anything bigger than median_item
            right = median_idx - 1
    
    return None

def binary_search_recursive(array, item, left=0, right=None):
    if right == None: # only called first time this function is called
        right = len(array) - 1
    elif left > right: # reached end of list
        return None
    
    median_idx = (left + right) // 2
    median_item = array[median_idx]

    if median_item == item:
        return median_idx
    elif median_item < item:
        left = median_idx + 1
    elif median_item > item:
        right = median_idx - 1
    
    return binary_search_recursive(array, item, left, right)
    