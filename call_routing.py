# partially pair programmed with github.com/alishalabi
import random # to generate random numbers
import re # for regular expressions
import sys # for command line args
import time # for benchmarking purposes

class CallRouter(object):
    def __init__(self, phone_numbers_path, route_prices_path):
          # Turn txt files (data sources) into python objects
          self.phone_numbers = self.parse_phone_numbers(phone_numbers_path)
          # Contains best price per unique prefix. Using a dict allows quick fetch AND update
          self.prices = {}
          # Parse routes which populates self.prefixes and self.prices
          self.parse_routes(route_prices_path)

    def turn_txt_file_into_array(self, path_to_file):
        """Turns txt file into list without '\n' or '+' characters"""
        array = open(path_to_file, 'r').read().split('\n') # split at each new line
        array.pop() # remove last item of array which is always empty due to new line at EOF
        return array

    def parse_phone_numbers(self, phone_numbers_path):
        """Turns txt file into list of phone numbers without the +"""
        return self.turn_txt_file_into_array(phone_numbers_path)
    
    def parse_routes(self, route_prices_path):
        """ Goes through route_prices_path and creates a binary tree """
        # Parse .txt file into a python array
        routes = self.turn_txt_file_into_array(route_prices_path)

        # For every route
        for route in routes:
            # get prefix and price (separated by a comma)
            prefix, price = route.split(',')

            if prefix in self.prices:
                # Check if price is cheaper
                if self.prices[prefix] > price:
                    self.prices[prefix] = price
            else: # We've never seen prefix before
                # self.prefixes.insert(prefix) # insert prefix into our list of prefixes
                self.prices[prefix] = price # log the cost for that prefix

    def get_routing_cost(self, phone_number):
        """Find longest matching prefix and return cheapest cost
        Since routes is a binary tree, we only remember cheapest cost for identical prefix"""
        last_digit_idx = len(str(phone_number)) - 1
        # Search for full phone number inside prefix, then remove one digit at a time
        while last_digit_idx > 0:
            substring = phone_number[0:last_digit_idx]
            if substring in self.prices:
                return self.prices[substring]
            last_digit_idx -= 1
        
        # If we have no matching routes, return 0
        else:
            return 0
    
    def save_routing_costs(self, phone_numbers):
        result = []

        for number in phone_numbers:
            cost = self.get_routing_cost(number)
            line = "{},{}".format(number, cost)
            result.append(line)
            # save number and cost to text file
        return result

def test_scenario_3():
    """This is a test for Scenario 3: Get costs for 10k phone numbers and 10M route costs"""
    start_time = time.time()
    phone_numbers_path = 'call-routing-files/phone-numbers-10000.txt' # 10K
    route_prices_path = 'call-routing-files/route-costs-10000000.txt' # 10M 
    # initalize the call router, which will begin parsing data sources its given automatically
    call_router = CallRouter(phone_numbers_path, route_prices_path)
    # Look up and print costs
    print(call_router.save_routing_costs(call_router.phone_numbers))
    print('total run time:', (time.time() - start_time))
    # Benchmarks on 2.7 GHz Intel Core i7 Processor w/ 16 GB 2133 MHz LPDDR3 RAM:
    # 1K Phone #s | 1M routes  | 1.1 seconds
    # 1K Phone #s | 10M routes | 11.3 seconds

def run_tests():
    

if __name__ == '__main__':
    test_scenario_3()