def get(vertices):
	'''
		function asking as parameter the list of vertices from graph
		gets the line graph and returns it
	'''
	res = []
	tmp_length = len(vertices)
	for i in range(1, tmp_length):
		index = vertices[0]
		vertices.remove(index)
		index.sort()
		for tmp_elem in vertices:
			tmp_elem.sort()
			if any(elem in tmp_elem  for elem in index):
				res.append([index, tmp_elem])
	return res