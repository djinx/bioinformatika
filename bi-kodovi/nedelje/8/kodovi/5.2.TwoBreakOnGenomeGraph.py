def two_break_on_genome_graph(genome_graph, i, ip, j, jp):

	new_edges = []
	
	for edge in genome_graph:
		if (edge[0] == i and edge[1] == ip) or (edge[0] == j and edge[1] == jp):
			continue
		new_edges.append(edge)
		
	new_edges.append((i,j))
	new_edges.append((ip,jp))
	
	return new_edges