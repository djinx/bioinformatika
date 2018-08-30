def HMM(strings_pos, strings_neg):
	HMM = {}

	for string in strings_pos:
		for i in range(1, len(string)):
			c_prev_state = string[i-1] + '+'
			c_curr = string[i]

			if c_prev_state not in HMM:
				HMM[c_prev_state] = {}
				HMM[c_prev_state]['state'] = 1
				HMM[c_prev_state]['nucleotide'] = string[i-1]
				HMM[c_prev_state]['transitions'] = {}

			if c_curr not in HMM[c_prev_state]['transitions']:
				HMM[c_prev_state]['transitions'][c_curr] = 0

			HMM[c_prev_state]['transitions'][c_curr] += 1

	for string in strings_neg:
		for i in range(1, len(string)):
			c_prev_state = string[i-1] + '-'
			c_curr = string[i]

			if c_prev_state not in HMM:
				HMM[c_prev_state] = {}
				HMM[c_prev_state]['state'] = 0
				HMM[c_prev_state]['nucleotide'] = string[i-1]
				HMM[c_prev_state]['transitions'] = {}

			if c_curr not in HMM[c_prev_state]['transitions']:
				HMM[c_prev_state]['transitions'][c_curr] = 0

			HMM[c_prev_state]['transitions'][c_curr] += 1

	for source in HMM:
		output_sum = 0
		for dest in HMM[source]['transitions']:
			output_sum += HMM[source]['transitions'][dest]
		for dest in HMM[source]['transitions']:
			HMM[source]['transitions'][dest] = (HMM[source]['transitions'][dest] / output_sum) * 0.98

		HMM[source]['0'] = 0.02
	return HMM