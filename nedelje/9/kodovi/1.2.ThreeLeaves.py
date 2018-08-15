def three_leaves(D, n):
	for i in range(n-1):
		for k in range(i, n-1):
			if D[i][k] == (D[i][n-1] + D[n-1][k]):
				return (i, n, k)