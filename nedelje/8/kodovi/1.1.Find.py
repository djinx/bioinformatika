def find(P, start, n):
	for i in range(start, len(P)):
		if P[i] == n or P[i] == -n:
			return i