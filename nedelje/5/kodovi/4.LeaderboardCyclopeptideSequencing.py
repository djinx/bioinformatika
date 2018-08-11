def leaderboard_cyclopeptide_sequencing(spectrum, N, amino_acid, amino_acid_mass):
    leaderboard = ['']
    leader_peptide = ''
    while len(leaderboard) > 0:
        next_leaderboard = []
        leaderboard = expand(leaderboard, amino_acid)
        next_leaderboard = copy.copy(leaderboard)
        for peptide in leaderboard:
            if mass(peptide, amino_acid, amino_acid_mass) == parent_mass(spectrum):
                if score(peptide, spectrum, amino_acid, amino_acid_mass) > score(leader_peptide, spectrum, amino_acid, amino_acid_mass):
                    leader_peptide = peptide
            elif mass(peptide, amino_acid, amino_acid_mass) > parent_mass(spectrum):
                next_leaderboard.remove(peptide)
        leaderboard = trim(next_leaderboard, spectrum, N, amino_acid, amino_acid_mass)
    return leader_peptide