# -----------------------------------------------------------------------------
# Christian Ricardo Solís Cortés & Eduardo Josué Contreras Álvarez
# A01063685
# Artificial Intelligence
# Assignment: Bayes Networks
# Querying a Bayes Network
# -----------------------------------------------------------------------------

import sys
import heapq
import itertools

# -----------------------------------------------------------------------------
# Parsing and cleaning process
# -----------------------------------------------------------------------------

# Clean initial string to get only the necessary info
def input_reading(initial_input):
    # Remove spaces from the input
    input_without_spaces = initial_input.read().replace(' ', '')
    # Split input by line breaks
    splited_input_by_line_break = input_without_spaces.split('\n')
    # Save nodes and number of probabilities in stack
    stack_of_nodes = splited_input_by_line_break[0]
    number_of_probabilities = int(splited_input_by_line_break[1])
    # Save probabilities in a list
    probabilities = list()
    for line in range(2, 2 + number_of_probabilities):
        probabilities.append(splited_input_by_line_break[line])
    # Save number of queries in stack
    number_of_queries = int(splited_input_by_line_break[2 + number_of_probabilities])
    # Save queries in a list
    queries = list()
    for line in range(3 + number_of_probabilities, 3 + number_of_probabilities + number_of_queries):
        queries.append(splited_input_by_line_break[line])

    print(stack_of_nodes)
    print(number_of_probabilities)
    print(probabilities)
    print(number_of_queries)
    print(queries)

# -----------------------------------------------------------------------------
# Main function
# -----------------------------------------------------------------------------

def main():
    bayes = open('test.in','r')
    input_reading(bayes)

if __name__ == '__main__':
    main()
