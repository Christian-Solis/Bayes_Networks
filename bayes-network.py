# -----------------------------------------------------------------------------
# Christian Ricardo Solís Cortés & Eduardo Josué Contreras Álvarez
# A01063685
# Artificial Intelligence
# Assignment: Bayes Networks
# Querying a Bayes Network
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Parsing and cleaning process
# -----------------------------------------------------------------------------

# Clean initial string to get only the nodes

def input_reading(initial_input):
    input_without_spaces = initial_input.replace(' ', '')

    # cont_stacks = list()
    # # split when a ';' is found
    # stacks = input_without_spaces.split(';')
    # for st in stacks:
    #     st = st.replace('(', '')
    #     st = st.replace(')', '')
    #     if st == '':
    #         cont_stacks.append(list())
    #     else:
    #         containers = st.split(',')
    #         cont_stacks.append(containers)
    # return cont_stacks

def main():
    bayes = input()
    input_reading(input)

    # read_probability_tables(bayes_net)
    # read_execute_queries(bayes_net)

if __name__ == '__main__':
    main()
