def UPGMA(D, n):
	clusters = [Cluster([i], 0) for i in range(n)]

	num_clusters = len(D)

	while num_clusters > 1:
		(i, j, distance) = min_distance(clusters, D, num_clusters)
		
		new_cluster = Cluster(clusters[i].elements + clusters[j].elements, distance/2)
		new_cluster.add_left(clusters[i])
		new_cluster.add_right(clusters[j])		

		new_clusters_list = []
		for c in range(num_clusters):
			if c != i and c != j:
				new_clusters_list.append(clusters[c])

		new_clusters_list.append(new_cluster)
		clusters = new_clusters_list[:]
		num_clusters -= 1
	
	return clusters[0]