def colored_edges(P):
    edges = []
    for chromosome in P:
        nodes = chromosome_to_cycle(chromosome)
        for j in range(len(chromosome)):
            edges.append((nodes[2*j+1], nodes[(2*j+2) % len(nodes)]))
            edges.append((nodes[(2*j+2) % len(nodes)], nodes[2*j+1]))
			
    return edges