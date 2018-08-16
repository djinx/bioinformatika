def BWT(s):
	matrix = []
	s += '$'

	for i in range(len(s)):
		matrix.append(s)
		s = s[1:] + s[0]

	matrix.sort()
	return [row[-1] for row in matrix]