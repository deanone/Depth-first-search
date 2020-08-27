from collections import deque
import pandas as pd
import numpy as np
import string


def load_graph(graph_file):
	graph = pd.read_csv(graph_file, header=None)
	graph = graph.values
	return graph


def dfs_non_recursive(graph_file, r):
	alphabet = list(string.ascii_uppercase)
	G = load_graph(graph_file)
	N = G.shape[0]
	discovered = np.zeros(N)
	stack = deque()
	stack.append(r)
	while stack:
		v = stack.pop()
		if not discovered[v]:
			print(alphabet[v], end = ' ')
			discovered[v] = 1
			neighbors = G[v, :].nonzero()[0]
			for neighbor in neighbors:
				stack.append(neighbor)


def main():
	graph_file = 'graph.csv'
	r = 0
	dfs_non_recursive(graph_file, r)


if __name__ == '__main__':
	main()