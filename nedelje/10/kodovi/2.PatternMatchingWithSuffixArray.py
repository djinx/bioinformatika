def pattern_matching_with_suffix_array(suffix_array, pattern):
	top = 0
	bottom = len(suffix_array)-1

	while top <= bottom:
		mid = (top + bottom) // 2

		if len(suffix_array[mid]) > len(pattern):
			if suffix_array[mid][:len(pattern)] == pattern:
				return find_neighborhood(suffix_array, mid, pattern)	

		if pattern < suffix_array[mid]:
			bottom = mid - 1
		else:
			top = mid + 1