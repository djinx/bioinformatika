def shortest_rearrangement_scenario(P, Q):
	red_edges = colored_edges([P])
	blue_edges = colored_edges([Q])
	
	num_of_breaks = 0

	while has_nontrivial_cycle(red_edges, blue_edges):	
		(j,i_p) = select_edge_from_nontrivial_cycle(red_edges, blue_edges)

		i = -1
		j_p = -1

		for (v,w) in red_edges:
		 	if v == j:
		 		i = w
		 	if w == j:
		 		i = v
		 	if v == i_p:
		 		j_p = w

		red_edges.remove((j, i))
		red_edges.remove((i, j))
		red_edges.remove((i_p, j_p))
		red_edges.remove((j_p, i_p))

		red_edges.append((j, i_p))
		red_edges.append((i_p, j))
		red_edges.append((j_p, i))
		red_edges.append((i, j_p))

		num_of_breaks += 1
  
  return num_of_breaks  