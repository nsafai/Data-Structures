from binarytree import BinarySearchTree, BinaryTreeNode
from hashtable import HashTable

class CallRouter(object):

    def __init__(self, phone_numbers_txt_files, route_prices_txt_files):
          # Turn txt files (data sources) into python objects
          self.phone_numbers = self.parse_phone_numbers(route_prices_txt_files)
          # binary tree of prefixes. Using a BST allows us to find longest prefix as fast as possible
          self.prefixes = BinarySearchTree()
          # self.prices contains best price per unique prefix. Using a dict allows quick fetch AND update
          self.prices = {}
          self.parse_routes(route_prices_txt_files)
          

    def parse_phone_numbers(self, route_prices_txt_files):
        # Turn into list without the "+"
        pass
    
    def parse_routes(self, route_prices_txt_files):
        """ Goes through route_prices_txt_files and creates a binary tree """
        prefix = ...
        if self.prefixes.contains(prefix):
            self.prefixes.inserT(prefix)
        
        # For every line in the file:
            # if line.prefix already in routes
                if prices[prefix]
        pass

    def routing_cost(phone_number)
        """Find longest matching prefix and return cheapest cost
        Since routes is a binary tree, we only remember cheapest cost for identical prefix"""
        best_route = None
        idx_last_digit_to_compare = len(phone_number) - 1
        while idx_last_digit_to_compare > 0:
            node = self.prefixes.contains(phone_number[:idx_last_digit_to_compare]):
            if node is 

        return best_route

    def prefix_in_number()