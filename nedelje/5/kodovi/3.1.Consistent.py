def consistent(peptide, target_spectrum, amino_acid, amino_acid_mass):
    peptide_linear_spectrum = linear_spectrum(peptide, amino_acid, amino_acid_mass)

    for aa in peptide_linear_spectrum:
        found = False
        for aa_p in target_spectrum:
            if aa_p == aa:
                found = True
        if found == False:
            return False
            
    return True