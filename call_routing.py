from binarytree import BinarySearchTree, BinaryTreeNode
from hashtable import HashTable

class CallRouter(object):

    def __init__(self, phone_numbers_txt_files, route_prices_txt_files):
          # Turn txt files (data sources) into python objects
          self.phone_numbers = self.parse_phone_numbers(phone_numbers_txt_files)
          # Binary tree of prefixes. Using a BST allows us to find longest prefix as fast as possible
          self.prefixes = BinarySearchTree()
          # Contains best price per unique prefix. Using a dict allows quick fetch AND update
          self.prices = {}
          # Parse routes which populates self.prefixes and self.prices
          self.parse_routes(route_prices_txt_files)
          # Look up costs
          self.save_routing_costs(self.phone_numbers)
          

    def parse_phone_numbers(self, phone_numbers_txt_files):
        """Turns txt file into list of phone numbers without the +"""
        phone_numbers = []
        for number in phone_numbers_txt_files:
            phone_numbers.append(number)
        return phone_numbers
    
    def parse_routes(self, route_prices_txt_files):
        """ Goes through route_prices_txt_files and creates a binary tree """
        # For every line of file
        for line in route_prices_txt_files:
            route = line.split(',')
            prefix = route[0]
            price = route[1]

            if self.prefixes.contains(prefix):
                # Check if price is cheaper
                if self.prices[prefix] > price:
                    self.prices[prefix] = price
            else: # We've never seen prefix before
                self.prefixes.insert(prefix) # insert prefix into our list of prefixes
                self.prices[prefix] = price # log the cost for that prefix

    def get_routing_cost(self, phone_number):
        """Find longest matching prefix and return cheapest cost
        Since routes is a binary tree, we only remember cheapest cost for identical prefix"""
        last_digit_idx = len(str(phone_number)) - 1
        # Search for full phone number inside prefix, then remove one digit at a time
        while last_digit_idx > 0:
            print(last_digit_idx)
            substring = phone_number[0:last_digit_idx]
            if self.prefixes.contains(substring):
                return self.prices[substring]
            last_digit_idx -= 1
        
        # If we have no matching routes, return 0
        else:
            return 0
    
    def save_routing_costs(self, phone_numbers):
        result = []

        for number in phone_numbers:
            print(number)
            cost = self.get_routing_cost(number)
            line = "{},{}".format(number, cost)
            result.append(line)
            # save number and cost to text file
        print(result)
        return result

phone_numbers = ["86153023841"]
routes = [
  "449275049,0.49",
  "86153,0.84",
  "8130,0.68",
  "4928843955,0.40",
  "449187847,0.48",
  "8197753,0.75",
  "449916707,0.58",
  "64655676,0.40",
  "8615302,1.54",
  "34924199,0.39",
  "1941613,0.05",
  "61312545,0.43",
  "8615302,1.84",
  "8615302,1.04"
]
call_router = CallRouter(phone_numbers, routes)