def isolated_cycle(G, v):
	cycle = []

	(in_deg, out_deg) = degree(G, v)

	while in_deg == 1 and out_deg == 1:
		u = G[v][0]
		cycle.append((v,u))
		if cycle[0][0] == cycle[-1][1]:
			return cycle

		v = u
		(in_deg, out_deg) = degree(G, v)

	return None