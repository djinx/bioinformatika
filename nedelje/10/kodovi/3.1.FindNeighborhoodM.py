def find_neighborhood(suffix_array, mid, pattern):
	up = mid
	down = mid

	while up >= 0 and len(suffix_array[up][0]) > len(pattern) and suffix_array[up][0][:len(pattern)] == pattern:

		up -= 1

	while down < len(suffix_array) and len(suffix_array[down][0]) > len(pattern) and suffix_array[down][0][:len(pattern)] == pattern:
		
		down += 1

	positions = []

	for i in range(up+1, down):
		positions.append((suffix_array[i][1], suffix_array[i][2]))

	positions.sort()
	return positions