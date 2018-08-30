def trie_matching(text, Trie):
	found_patterns = []
	while len(text) > 0:
		res = prefix_trie_pattern_matching(text, Trie)
		if res != False:
			found_patterns.append(res)
		text = text[1:]
	return found_patterns