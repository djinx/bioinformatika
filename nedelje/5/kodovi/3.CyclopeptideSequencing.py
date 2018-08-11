def cyclopeptide_sequencing(spectrum, amino_acid, amino_acid_mass):
    peptides = ['']
    i = 1
    while len(peptides) > 0:
        next_peptides = []
        peptides = expand(peptides, amino_acid)
        next_peptides = copy.copy(peptides)
        for peptide in peptides:
            if mass(peptide, amino_acid, amino_acid_mass) == parent_mass(spectrum):
                if cyclic_spectrum(peptide, amino_acid, amino_acid_mass) == spectrum:
                    print(peptide)
                next_peptides.remove(peptide)
            elif not consistent(peptide, spectrum, amino_acid, amino_acid_mass):
                next_peptides.remove(peptide)
        peptides = next_peptides