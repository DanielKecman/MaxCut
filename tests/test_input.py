import unittest
from max_cut_solver.input_utils import get_num_nodes_and_edges_from_dictionary, read_data_from_json

class InputTest(unittest.TestCase):
    def test_input(self):
        input_dict = self._get_good_test_dictionary()
        num_nodes, edges = get_num_nodes_and_edges_from_dictionary(input_dict)
        print(num_nodes)
        print(edges)

    def test_file_input(self):
        filename = "..\data_file.txt"

        data = read_data_from_json(filename)

        num_nodes, edges = get_num_nodes_and_edges_from_dictionary(data)
        print(num_nodes)
        print(edges)

    def test_bad_input_one(self):
        input = self._get_bad_input_one()
        with self.assertRaisesRegex(ValueError, "Couldn't find key for number of nodes"):
            num_nodes, edges = get_num_nodes_and_edges_from_dictionary(input)

    def test_bad_input_two(self):
        input = self._get_bad_input_two()
        with self.assertRaisesRegex(ValueError, "Number of nodes should be an integer, but given <class 'str'>"):
            num_nodes, edges = get_num_nodes_and_edges_from_dictionary(input)

    def test_bad_input_three(self):
        input = self._get_bad_input_three()
        with self.assertRaisesRegex(ValueError, "Couldn't find key for edges"):
            num_nodes, edges = get_num_nodes_and_edges_from_dictionary(input)

    def test_bad_input_four(self):
        input = self._get_bad_input_four()
        with self.assertRaisesRegex(ValueError, "Dictionary expected for edges, but got <class 'dict'>"):
            num_nodes, edges = get_num_nodes_and_edges_from_dictionary(input)

    def test_bad_input_five(self):
        input = self._get_bad_input_five()
        with self.assertRaisesRegex(ValueError, "Dictionary expected, but got <class 'list'>"):
            num_nodes, edges = get_num_nodes_and_edges_from_dictionary(input)

    def _get_bad_input_one(self):
        return {
            "edges": {
                "0": {
                    "1": 1,
                    "2": 1
                },
                "1": {
                    "3": 1
                },
                "2": {
                    "3": 1,
                    "4": 1
                },
                "3": {
                    "4": 1
                }
            }
        }

    def _get_bad_input_two(self):
        return {
            "num_nodes": "two",
            "edges": {
                "0": {
                    "1": 1
                }
            }
        }

    def _get_bad_input_three(self):
        return {
            "num_nodes": 3
        }

    def _get_bad_input_four(self):
        return {
            "num_nodes": 3,
            "edges": [(0, 1, 1), (0, 2, 1), (1, 2, 1)]
        }

    def _get_bad_input_five(self):
        return [(0, 1, 1), (0, 2, 1), (1, 2, 1)]

    def _get_good_test_dictionary(self):
        return {
            "num_nodes": 5,
            "edges": {
                "0": {
                    "1": 1,
                    "2": 1
                },
                "1": {
                    "3": 1
                },
                "2": {
                    "3": 1,
                    "4": 1
                },
                "3": {
                    "4": 1
                }
            }
        }

if __name__ == '__main__':
    unittest.main()
