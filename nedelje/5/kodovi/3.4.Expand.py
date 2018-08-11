def expand(peptides, amino_acid):
    extension = []

    for peptide in peptides:
        for aa in amino_acid:
            extension.append(peptide + aa)
        
    return extension