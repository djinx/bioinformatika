def viterbi(HMM, string):

	matrix = [{} for i in range(len(string))]
	path = ""

	for i in range(len(string)):
		nucleotide = string[i]

		if i > 0:
			path += max_transition_state

		max_transition_prob = -1
		max_transition_state = ''

		for state in HMM:

			if HMM[state]['nucleotide'] != nucleotide:
				matrix[i][state] = 0

			elif i == 0:
				if HMM[state]['nucleotide'] == nucleotide:
					matrix[i][state] = 0.125

			else:
				max_prev = -1
				max_prev_state = ''

				for prev_state in matrix[i-1]:
					if HMM[prev_state]['state'] == HMM[state]['state']:
						state_change_prob = 0.99
					else:
						state_change_prob = 0.01

					if HMM[state]['nucleotide'] in HMM[prev_state]['transitions']:
						transition_prob = HMM[prev_state]['transitions'][HMM[state]['nucleotide']]
					else:
						transition_prob = 0

					curr_state = matrix[i-1][prev_state] * transition_prob * state_change_prob

					if curr_state > max_prev:
						max_prev = curr_state
						max_prev_state = prev_state

				matrix[i][state] = max_prev

				if max_prev > max_transition_prob:
					max_transition_prob = max_prev
					max_transition_state = max_prev_state

	max_end = -1
	max_end_state = ''
	
	n = len(string)
	for state in matrix[n-1]:
		if matrix[n-1][state] > max_end:
			max_end = matrix[n-1][state]
			max_end_state = state

	path += max_end_state
	return path