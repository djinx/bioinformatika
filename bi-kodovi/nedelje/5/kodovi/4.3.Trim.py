def trim(leaderboard, spectrum, N, amino_acid, amino_acid_mass):
	linear_scores = []
	for j in range(len(leaderboard)):
		peptide = leaderboard[j]
		linear_scores.append(linear_score(peptide, spectrum, amino_acid, amino_acid_mass))

	leaderboard_zipped = list(zip(linear_scores, leaderboard))
	leaderboard_zipped.sort(reverse=True)

	leaderboard = [el[1] for el in leaderboard_zipped]
	for j in range(N, len(leaderboard_zipped)):
		if leaderboard_zipped[j][0] < leaderboard_zipped[N-1][0]:
			leaderboard = [el[1] for el in leaderboard_zipped[:j]]
			return leaderboard
	return leaderboard