def find_insertion_point(path, distance):
	current_distance = 0
	previous_vertex = path[0][0]

	for i in range(1, len(path)):
		v = path[i][0]
		e = path[i][1]

		current_distance += e
		next_vertex = v
		
		
		if distance <= current_distance:
			return (previous_vertex, next_vertex, e, current_distance - distance)

		previous_vertex = v