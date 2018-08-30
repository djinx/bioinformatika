def last_to_first(first_column, c, count):
	for i in range(len(first_column)):
		if first_column[i] == c:
			if count == 1:
				return i
			count -= 1