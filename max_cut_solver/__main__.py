import numpy as np
import argparse

from max_cut_solver.optimization_solver import OptimizationSolver
from max_cut_solver.input_utils import get_number_of_nodes, get_edges, get_num_nodes_and_edges_from_json
from max_cut_solver.linalg_utils import get_square_root_of_matrix, random_vector
import traceback

if __name__ == "__main__":

    print("This solver solves the max cut problem using semi-definite programming:")
    print("")

    parser = argparse.ArgumentParser()
    parser.add_argument("--input_file")
    args = parser.parse_args()

    try:
        num_nodes = 0
        edges = []

        if args.input_file:
            num_nodes, edges = get_num_nodes_and_edges_from_json(args.input_file)
        else:
            num_nodes = get_number_of_nodes()
            edges = get_edges()

        solver = OptimizationSolver(num_nodes,
                                    edges)

        result, status, variables = solver.solve_problem()

        node_vector = get_square_root_of_matrix(variables)
        assignment_vector = random_vector(num_nodes)

        node_assignments = np.sign(node_vector @ assignment_vector)

        print()
        print("Optimization Complete!")
        print("Problem Status:", status)
        print("Optimal value:", result)
        print("Optimal variables:\n", variables)

        print("Node assignments use the square root vector of our "
              "decision matrix and map it onto a randomly generated hyperplane")
        print("Vector square root of decision matrix:\n", node_vector)
        print("Vector normal to our random hyperplane:\n", assignment_vector)
        print("Final assignments (+1 or -1):\n", node_assignments)



    except Exception as e:
        print(f"Optimization solver failed due to : {repr(e)}")
        print(traceback.format_exc())


