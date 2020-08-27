from collections import deque
import pandas as pd
import numpy as np
import string


def load_graph(graph_file):
	"""
	The graph is stored in a .csv file in the form of an adjacency matrix.

	:param graph_file: the name of the graph .csv file
	:type graph_file: String
	:return: the graph as adjacency matrix
	:rtype: numpy.ndarray
	"""

	graph = pd.read_csv(graph_file, header=None)
	graph = graph.values
	return graph


def dfs_non_recursive(graph_file, r):
	"""
	The non-recursive implementation of the DFS algorithm.

	:param graph_file: the name of the graph .csv file
	:type graph_file: String
	:param r: the root node of the graph
	:type r: int
	:return: an ordered list of the nodes of the graph
	:rtype: list
	"""

	traversed_nodes = []
	alphabet = list(string.ascii_uppercase)
	G = load_graph(graph_file)
	N = G.shape[0]
	discovered = np.zeros(N)
	stack = deque()
	stack.append(r)
	while stack:
		v = stack.pop()
		if not discovered[v]:
			traversed_nodes.append(alphabet[v])
			discovered[v] = 1
			neighbors = G[v, :].nonzero()[0]
			for neighbor in neighbors:
				stack.append(neighbor)
	return traversed_nodes


def main():
	"""
	The main function.
	
	"""

	graph_file = 'graph.csv'
	r = 0
	traversed_nodes = dfs_non_recursive(graph_file, r)
	for node in traversed_nodes:
		print(node, end = ' ')


if __name__ == '__main__':
	main()