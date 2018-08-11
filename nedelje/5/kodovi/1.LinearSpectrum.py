def linear_spectrum(peptide, amino_acid, amino_acid_mass):
    prefix_mass = [0]
    current_mass = 0
    for i in range(len(peptide)):
        for j in range(20):
            if amino_acid[j] == peptide[i]:
                prefix_mass.append(current_mass + amino_acid_mass[j])
                current_mass += amino_acid_mass[j]
                
    linear_spectrum = [0]
    for i in range(len(prefix_mass)):
        for j in range(i+1, len(prefix_mass)):
            linear_spectrum.append(prefix_mass[j] - prefix_mass[i])
            
    linear_spectrum.sort()
    return linear_spectrum