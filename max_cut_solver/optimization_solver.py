import cvxpy as cp


class OptimizationSolver:
    def __init__(self,
                 num_nodes: int,
                 edges: list[tuple[int, int, float]]):

        self._num_nodes = num_nodes
        self._edges = edges
        self._validate_inputs()

        self._variables = self._create_variables()
        self._constraints = self._create_constraints()

    def _validate_inputs(self):
        num_edges = len(self._edges)

        if num_edges == 0:
            raise ValueError(f"No edges provided, no problem to solve")

        found_invalid_edge = False
        error_messages = []
        already_found_nodes = {}
        for start_node, end_node, weight in self._edges:
            if start_node < 0:
                found_invalid_edge = True
                error_messages.append(f"Found edge start node {start_node} that is "
                                      f"negative in edge ({start_node}, {end_node})")
            if end_node < 0:
                found_invalid_edge = True
                error_messages.append(f"Found edge end node {start_node} that is "
                                      f"negative in edge ({start_node}, {end_node})")
            if start_node >= self._num_nodes:
                found_invalid_edge = True
                error_messages.append(f"Found reference to start node {start_node} that is larger "
                                      f"than given number of nodes {self._num_nodes}")
            if end_node >= self._num_nodes:
                found_invalid_edge = True
                error_messages.append(f"Found reference to end node {end_node} that is larger "
                                      f"than given number of nodes {self._num_nodes}")

            # TO DO find if any duplicates
            if start_node in already_found_nodes.keys():
                if end_node in already_found_nodes[start_node]:
                    found_invalid_edge = True
                    error_messages.append(f"Duplicate edge ({start_node}, {end_node}) found")
                else:
                    already_found_nodes[start_node].append(end_node)
            else:
                already_found_nodes[start_node] = [end_node]

            if end_node in already_found_nodes.keys() and start_node in already_found_nodes[end_node]:
                found_invalid_edge = True
                error_messages.append(f"Found reverse edges ({start_node}, {end_node}) and ({end_node}, {start_node})")

        if found_invalid_edge:
            all_error_messages = "\n".join(message for message in error_messages)
            raise ValueError(all_error_messages)

    def _create_variables(self):
        return cp.Variable((self._num_nodes, self._num_nodes), PSD=True)

    def _create_constraints(self):
        constraints = [self._variables >> 0]
        for i in range(self._num_nodes):
            constraints.append(self._variables[i, i] == 1)

        return constraints

    def _create_objective_function(self):
        cut_value = 0
        for start_node, end_node, weight in self._edges:
            cut_value += cp.multiply(0.5, cp.multiply(weight, 1 - self._variables[start_node, end_node]))

        return cut_value

    def solve_problem (self):
        problem = cp.Problem(cp.Maximize(self._create_objective_function()), self._constraints)
        return problem.solve(), problem.status, self._variables.value
