# -----------------------------------------------------------------------------
# Christian Ricardo Solís Cortés & Eduardo Josué Contreras Álvarez
# A01063685
# Artificial Intelligence
# Assignment: Bayes Networks
# Querying a Bayes Network
# -----------------------------------------------------------------------------

import heapq
import itertools
import sys

# -----------------------------------------------------------------------------
# Parsing and cleaning process
# -----------------------------------------------------------------------------

# Clean initial string to get only the necessary info
def input_reading(initial_input):
    # Remove spaces from the input
    input_without_spaces = initial_input.read().replace(' ', '')
    # Split input by line breaks
    splitted_input_by_line_break = input_without_spaces.split('\n')
    # Save nodes and number of probabilities in stack
    stack_of_nodes = splitted_input_by_line_break[0]
    number_of_probabilities = int(splitted_input_by_line_break[1])
    # Save probabilities in a list
    probabilities = list()
    for line in range(2, 2 + number_of_probabilities):
        probabilities.append(splitted_input_by_line_break[line])
    # Save number of queries in stack
    number_of_queries = int(splitted_input_by_line_break[2 + number_of_probabilities])
    # Save queries in a list
    queries = list()
    for line in range(3 + number_of_probabilities, 3 + number_of_probabilities + number_of_queries):
        queries.append(splitted_input_by_line_break[line])

    # print(stack_of_nodes)
    # print(number_of_probabilities)
    # print(probabilities)
    # print(number_of_queries)
    # print(queries)

    # Send respective values to functions
    split_nodes(stack_of_nodes)
    split_probabilites(probabilities)
    split_queries(queries)

    #return(stack_of_nodes, number_of_probabilities, probabilities, number_of_queries, queries)

# -----------------------------------------------------------------------------
# Step One: Split the nodes by comma
# Return: list_of_nodes
# -----------------------------------------------------------------------------

def split_nodes(stack_of_nodes):
    # Split the nodes by comma and save in list_of_nodes
    list_of_nodes = stack_of_nodes.split(',')
    return(list_of_nodes)

# -----------------------------------------------------------------------------
# Step Two: Split the probabilities by =
# Return: splitted_probabilites
# -----------------------------------------------------------------------------

def split_probabilites(probabilities):
    # Split probabilities by = and save in dictionary
    splitted_probabilites = {}
    for prob in probabilities:
        single_prob = prob.split('=')
        # Save splitted single_prob into dictionary and convert prob to float
        splitted_probabilites[single_prob[0]] = float(single_prob[1])

    return(splitted_probabilites)

# -----------------------------------------------------------------------------
# Step Three: Split the queries by given (|)
# Return: queries_with_given and queries_without_given
# -----------------------------------------------------------------------------

def split_queries(queries):
    # Split queries if a given (|) is found
    queries_with_given = list()
    queries_without_given = list()
    for query in queries:
        # If find returns -1 given is found
        if query.find('|') != -1:
            queries_with_given.append(query)
        else:
            queries_without_given.append(query)

    return(queries_with_given)
    return(queries_without_given)

# -----------------------------------------------------------------------------
# Testing function
# Print what I have so far
# -----------------------------------------------------------------------------

# def testing(list_of_nodes, splitted_probabilites, queries_with_given, queries_without_given):
#     print(list_of_nodes)
#     print(splitted_probabilites)
#     print(queries_with_given)
#     print(queries_without_given)

# -----------------------------------------------------------------------------
# Node class with everything together
# -----------------------------------------------------------------------------

class Node:

	def _init_(self, name, parents, table):
		self.name = name
		self.parents = parents
		self.table = table

    # def __str__(self):
    #     return self.name

# -----------------------------------------------------------------------------
# Step four: Calculate probability
# Return: total_probability
# -----------------------------------------------------------------------------

def calculate_probability(queries_with_given, queries_without_given):
    # Separate calculation into numerator and denominator
    numerator = 0
    denominator = 0
    total_probability = numerator / denominator

    # Set denominator as cero if a querie has no given
    # if !queries_with_given:
    #     denominator = 0

    return total_probability

# -----------------------------------------------------------------------------
# Main function
# -----------------------------------------------------------------------------

def main():
    bayes = open('test.in','r')
    input_reading(bayes)

if __name__ == '__main__':
    main()
