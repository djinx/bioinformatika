def find_path(T, start, stop):
	path = [(start, 0)]
	visited = {}
	visited[start] = True

	while len(path) > 0:
		v = path[-1][0]
		
		if v == stop:
			return path

		found = False

		for (w,e) in T[v]:
			if w not in visited:
				path.append((w,e))
				visited[w] = True
				found = True
				break

		if not found:
			path.pop()
	
	return []