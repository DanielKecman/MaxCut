import numpy as np
from max_cut_solver.validation_utils import validate_non_negative_number, validate_positive_number

def get_int(prompt, validation_function = None):
    while True:
        val_str = input(prompt)
        try:
            val = int(val_str)
            if validation_function != None:
                validation_function(val)
            return val
        except Exception as e:
            print(f"You entered invalid value <{val_str}> ({repr(e)}), please re-enter valid value")

def get_float(prompt, validation_function = None):
    while True:
        val_str = input(prompt)
        try:
            val = float(val_str)
            if validation_function != None:
                validation_function(val)
            return val
        except Exception as e:
            print(f"You entered invalid value <{val_str}> ({repr(e)}), please re-enter valid value")

def get_number_of_nodes():
    num_vars = get_int("Enter the number of nodes in your graph: ", validate_positive_number)
    return num_vars

def get_edges():
    edges = []

    print("Input the edges of the graph:")
    add_edges = 'yes'
    while add_edges in ['y', 'yes']:
        starting_node = get_int("Enter the starting node:", validate_non_negative_number)
        ending_node = get_int("Enter the ending node:", validate_non_negative_number)
        weight = get_float("Enter the edge weight")

        edges.append((starting_node, ending_node, weight))

        add_edges = input("Do you want to add more edges? (yes/no): ").strip().lower()
    return edges

