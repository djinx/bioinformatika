def suffix_array_construction(string):
	suffix_array = []
	string += '$'

	for i in range(len(string)):
		suffix_array.append(string[i:])

	suffix_array.sort()
	return suffix_array