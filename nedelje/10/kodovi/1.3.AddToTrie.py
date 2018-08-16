def add_to_trie(Trie, pattern, number_of_nodes, pattern_id):
	current_node = 'root'

	for c in pattern:
		if c in Trie[current_node]:
			current_node = Trie[current_node][c]
		else:
			if c != '$':
				Trie['i'+str(number_of_nodes)] = {}
				Trie[current_node][c] = 'i'+str(number_of_nodes)
				current_node = 'i'+str(number_of_nodes)
				number_of_nodes += 1
			else:
				Trie[current_node][c] = pattern_id
				Trie[pattern_id] = {}

	return (Trie, number_of_nodes)