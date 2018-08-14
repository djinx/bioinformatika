def two_break_on_genome(P, i, ip, j, jp):
	genome_graph = black_edges(P) + colored_edges([P])
	genome_graph = two_break_on_genome_graph(genome_graph, i, ip, j, jp)
	
	P = graph_to_genome(genome_graph)
	
	return P