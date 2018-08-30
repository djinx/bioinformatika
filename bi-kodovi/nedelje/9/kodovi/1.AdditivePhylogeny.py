def additive_phylogeny(D, n):
	if n == 2:
		return {
			0: [(1, D[0][1])],
			1: [(0, D[1][0])]
		}

	limb_length = limb(D, n-1)

	for j in range(n-1):
		D[j][n-1] = D[j][n-1] - limb_length
		D[n-1][j] = D[j][n-1]

	(i, n, k) = three_leaves(D, n)

	x = D[i][n-1]

	T = additive_phylogeny(D, n - 1)

	(T, v) = insert_vertex_on_path(T, i, k, x)

	T[v].append((n-1, limb_length))
	T[n-1] = [(v, limb_length)]

	return T
	
