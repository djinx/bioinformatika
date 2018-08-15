def min_distance(clusters, D, num_clusters):

	minimum = float('inf')
	min_i = -1
	min_j = -1

	for i in range(num_clusters):
		for j in range(i+1, num_clusters):
			dist = distance(D, clusters[i], clusters[j])
			if dist < minimum:
				minimum = dist
				min_i = i
				min_j = j

	return (min_i, min_j, minimum)