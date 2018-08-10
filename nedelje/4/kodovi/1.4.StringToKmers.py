def string_to_k_mers(dna_string, k):
	k_mers = []

	for i in range(len(dna_string) - (k-1)):
		k_mer = dna_string[i:i+k]
		k_mers.append(k_mer)

	return k_mers