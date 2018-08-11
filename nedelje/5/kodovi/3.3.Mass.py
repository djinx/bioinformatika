def mass(peptide, amino_acid, amino_acid_mass):
    total_mass = 0

    for i in range(len(peptide)):
        for j in range(len(amino_acid)):
            if peptide[i] == amino_acid[j]:
                total_mass += amino_acid_mass[j]
                
    return total_mass