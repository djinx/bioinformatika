def score(peptide, spectrum_2, amino_acid, amino_acid_mass):
	p1 = 0
	p2 = 0
	score = 0
	
	spectrum_1 = cyclic_spectrum(peptide, amino_acid, amino_acid_mass)
	
	while p1 < len(spectrum_1) and p2 < len(spectrum_2):
		if spectrum_1[p1] == spectrum_2[p2]:
			score += 1
			p1 += 1
			p2 += 1
		elif spectrum_1[p1] < spectrum_2[p2]:
			p1 += 1
		else:
			p2 += 1
			
	return score