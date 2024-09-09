This is a solver for the max cut problem for undirected graphs that uses semidefinite programming.

The solver takes in 2 versions of inputs:

- If not data file is provided, you will be prompted to provide the number of nodes in your graph, followed by the edges. Each edge will ask for a starting node, an ending node, and a weight.
- This information can also be provided in an input file, formatted as a json file like the following, where values in quotes should be given as strings, and all values in brackets are to be replaced with their actual values:

{
	"num_nodes" : (num_nodes)
	"edges": {
		"(starting_node)": {
			"(ending_node)": (weight),
   			"(ending_node)": (weight)
		}
	}
}

Since this is for undirected graphs, to avoid double counting errors will be thrown if the same edge is counted twice. This goes for assigning the same edge with two values (ex. (0, 1) with weight 1 and (0, 1) with weight 2)
as well as providing an edge with its reverse equal (ex. (0, 1) with weight 1 and (1, 0) with weight 1) so only provide one weight for each weight.

As mentioned above, the formulation stems from semidefinite programming, and in particular the Goemans-Williamson Max-Cut Algorithm, which can be found here https://math.mit.edu/~goemans/PAPERS/maxcut-jacm.pdf.
