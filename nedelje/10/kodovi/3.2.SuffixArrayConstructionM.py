def suffix_array_construction(strings):
	suffix_array = []

	for s in range(len(strings)):
		string = strings[s] + '$'
		for i in range(len(string)):
			suffix_array.append((string[i:],s, i))

	suffix_array.sort()
	return suffix_array