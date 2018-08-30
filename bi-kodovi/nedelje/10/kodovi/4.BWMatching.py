def bw_matching(first_column, last_column, pattern):
	top = 0
	bottom = len(last_column) - 1

	while top <= bottom:
		if len(pattern) > 0:
			symbol = pattern[-1]
			pattern = pattern[:-1]

			subset = last_column[top:bottom+1]
			
			if subset.index(symbol) != -1:
				top_index = -1
				bottom_index = -1

				for i in range(top, bottom+1):
					if symbol == last_column[i]:
						if top_index == -1:
							top_index = i
						bottom_index = i

				top_count = 0

				for i in range(top_index+1):
					if last_column[i] == symbol:
						top_count += 1

				bottom_count = top_count

				for i in range(top_index+1, bottom_index + 1):
					if last_column[i] == symbol:
						bottom_count += 1

				top = last_to_first(first_column, last_column[top_index], top_count)
				bottom = last_to_first(first_column, last_column[bottom_index], bottom_count)

			else:
				return 0

		else:
			return bottom - top + 1