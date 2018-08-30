def insert_vertex_on_path(T, start, stop, distance):
	path = find_path(T, start, stop)
	(v, w, e, e_dist) = find_insertion_point(path, distance)
	if e_dist == 0:
		return (T, w)

	T[v].remove((w, e))
	T[w].remove((v, e))
	new_v = str(v) + str(w) + str(e_dist)
	T[new_v] = []
	T[new_v].append((w, e_dist))
	T[w].append((new_v, e_dist))
	T[new_v].append((v, e - e_dist))
	T[v].append((new_v, e - e_dist))

	return (T, new_v)