def get(edges):
	'''
		function asking as parameter the list of edges from graph
		gets the line graph and returns it
	'''
	res = []
	tmp_length = len(edges)
	for i in range(1, tmp_length):
		index = edges[0]
		edges.remove(index)
		index.sort()
		for tmp_elem in edges:
			tmp_elem.sort()
			if any(elem in tmp_elem  for elem in index):
				res.append([index, tmp_elem])
	return res