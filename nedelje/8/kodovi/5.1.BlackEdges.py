def black_edges(P):
	nodes = chromosome_to_cycle(P)
	
	edges = []
	
	i = 0;
	
	while i < len(nodes):
		if nodes[i] < nodes[i+1]:
			edges.append((nodes[i], nodes[i+1]))
		else:
			edges.append((nodes[i+1], nodes[i]))
			
		i = i + 2
		
	return edges