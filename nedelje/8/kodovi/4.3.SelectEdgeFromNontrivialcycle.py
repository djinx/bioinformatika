def select_edge_from_nontrivial_cycle(P, Q):
	for (v,w) in Q:
		if (v,w) not in P and (w,v) not in P:
			return (v,w)