import json
from max_cut_solver.validation_utils import validate_non_negative_number, validate_positive_number

def is_int(value):
    try:
        val = int(value)
        return True

    except Exception as e:
        return False


def is_float(value):
    try:
        val = float(value)
        return True

    except Exception as e:
        return False

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
        starting_node = get_int("Enter the starting node: ", validate_non_negative_number)
        ending_node = get_int("Enter the ending node: ", validate_non_negative_number)
        weight = get_float("Enter the edge weight: ")

        edges.append((starting_node, ending_node, weight))

        add_edges = input("Do you want to add more edges? (yes/no): ").strip().lower()
    return edges

def get_num_nodes_and_edges_from_dictionary(input):

    if not isinstance(input, dict):
        raise ValueError(f"Dictionary expected, but got {type(input)}")

    if "num_nodes" not in input.keys():
        raise ValueError("Couldn't find key for number of nodes")

    num_nodes = input["num_nodes"]

    if not is_int(num_nodes):
        raise ValueError(f"Number of nodes should be an integer, but given {type(num_nodes)}")

    if "edges" not in input.keys():
        raise ValueError("Couldn't find key for edges")

    edges_dict = input["edges"]

    if not isinstance(edges_dict, dict):
        raise ValueError(f"Dictionary expected for edges, but got {type(input)}")

    edges = []

    for start_node in edges_dict.keys():
        if not isinstance(edges_dict[start_node], dict):
            raise ValueError(f"Dictionary expected for edge connections, but got {type(input)}")

        for end_node in edges_dict[start_node].keys():
            edge_weight = edges_dict[start_node][end_node]

            if not is_float(edge_weight):
                raise ValueError(f"Expected float for edge weight, but got {type(edge_weight)}")

            edges.append((int(start_node), int(end_node), float(edge_weight)))

    return num_nodes, edges

def read_data_from_json(file_name):
    with open(file_name, 'r') as file:
        data = json.load(file)

    return data

def get_num_nodes_and_edges_from_json(file_name):
    data = read_data_from_json(file_name)
    return get_num_nodes_and_edges_from_dictionary(data)
