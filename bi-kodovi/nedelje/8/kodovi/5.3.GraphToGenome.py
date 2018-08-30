def graph_to_genome(genome_graph):
	P = []
	nodes = []
	
	for (i,j) in genome_graph:
		nodes.append(i)
		nodes.append(j)
	
	
	prvi = [nodes[-1]]
	ostatak = copy.copy(nodes[:-1])
	nodes = prvi + ostatak
	
	chromosome = cycle_to_chromosome(nodes)
	P.append(chromosome)
		
	return P