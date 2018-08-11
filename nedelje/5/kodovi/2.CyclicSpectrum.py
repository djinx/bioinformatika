def cyclic_spectrum(peptide, amino_acid, amino_acid_mass):
    prefix_mass = [0]
    current_mass = 0
    for i in range(len(peptide)):
        for j in range(20):
            if amino_acid[j] == peptide[i]:
                prefix_mass.append(current_mass + amino_acid_mass[j])
                current_mass += amino_acid_mass[j]
                
    peptide_mass = prefix_mass[-1]
    cyclic_spectrum = [0]
    for i in range(len(prefix_mass)):
        for j in range(i+1, len(prefix_mass)):
            cyclic_spectrum.append(prefix_mass[j] - prefix_mass[i])
            if i > 0 and j < len(prefix_mass)-1:
                cyclic_spectrum.append(peptide_mass - 
                    (prefix_mass[j] - prefix_mass[i]))
            
    cyclic_spectrum.sort()
    return cyclic_spectrum