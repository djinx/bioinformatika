def find_neighborhood(suffix_array, mid, pattern):
	up = mid
	down = mid

	while up >= 0 and len(suffix_array[up]) > len(pattern) and suffix_array[up][:len(pattern)] == pattern:

		up -= 1

	while down < len(suffix_array) and len(suffix_array[down]) > len(pattern) and suffix_array[down][:len(pattern)] == pattern:
		
		down += 1

	positions = []

	for i in range(up+1, down):
		positions.append(len(suffix_array) - len(suffix_array[i]))

	positions.sort()
	return positions