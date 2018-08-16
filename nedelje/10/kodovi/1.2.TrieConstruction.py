def trie_construction(patterns):
	Trie = {}
	Trie['root'] = {}

	number_of_nodes = 1

	for i in range(len(patterns)):
		pattern = patterns[i]
		(Trie, number_of_nodes) = add_to_trie(Trie, pattern+'$', number_of_nodes, i)

	return Trie