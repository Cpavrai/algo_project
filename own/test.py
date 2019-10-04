import line_graph

'''
	"ensemble" variable will contain all the vertices from the graph
	by the formate following : a tuple containing two variables, the
	two ids of the edges from this vertex
'''

ensemble = [
	[1, 2],
	[1, 3],
	[1, 4],
	[2, 5],
	[3, 4],
	[4, 5]
]

result = line_graph.get(ensemble)

for elem in result:
	print(elem)