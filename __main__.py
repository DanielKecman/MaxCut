from max_cut_solver.optimization_solver import OptimizationSolver
from max_cut_solver.input_utils import get_number_of_nodes, get_edges
import traceback

if __name__ == "__main__":

    print("This solver solves the max cut problem using semi-definite programming:")
    print("")

    try:
        num_nodes = get_number_of_nodes()

        edges = get_edges()

        solver = OptimizationSolver(num_nodes,
                                    edges)

        result, status, variables = solver.solve_problem()

        print()
        print("Optimization Complete!")
        print("Problem Status:", status)
        print("Optimal value:", result)
        print("Optimal variables:", variables)

    except Exception as e:
        print(f"Optimization solver failed due to : {repr(e)}")
        print(traceback.format_exc())


