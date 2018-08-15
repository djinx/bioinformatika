def limb(D, j):
	
	minimum = float('inf')

	for i in range(j):
		for k in range(i+1, j):
			dist = (D[i][j] + D[j][k] - D[i][k])/2
			if dist < minimum:
				minimum = dist
	
	return int(minimum)