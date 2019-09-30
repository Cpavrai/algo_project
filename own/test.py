import line_graph

ensemble = [
	[1, 2],
	[1, 3],
	[1, 4],
	[2, 5],
	[3, 4],
	[4, 5]
]

result = line_graph.get(ensemble)

for r in result:
	print(r)