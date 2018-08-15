def distance(D, cluster_1, cluster_2):
	d = 0
	n1 = len(cluster_1.elements)
	n2 = len(cluster_2.elements)

	for i in cluster_1.elements:
		for j in cluster_2.elements:
			d += D[i][j]

	return d/(n1*n2)