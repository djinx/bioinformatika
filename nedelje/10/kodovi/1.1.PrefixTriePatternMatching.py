def prefix_trie_pattern_matching(text, Trie):
	v = 'root'

	for c in text:
		if c not in Trie[v]:
			return False

		v = Trie[v][c]

		if '$' in Trie[v]:
			return Trie[v]['$']

	return False