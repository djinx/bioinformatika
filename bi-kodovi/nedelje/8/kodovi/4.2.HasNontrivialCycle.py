def has_nontrivial_cycle(P, Q):
	for (v,w) in P:
		if (v,w) not in Q and (w,v) not in Q:
			return True

	return False