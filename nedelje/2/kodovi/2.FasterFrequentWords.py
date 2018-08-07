def faster_frequent_words(text, k):
    frequent_patterns = set([])
    
    frequency_array = computing_frequencies(text, k)
    
    max_count = max(frequency_array)
    
    for i in range(4**k):
        if frequency_array[i] == max_count:
            pattern = number_to_pattern(i, k)
            frequent_patterns.add(pattern)
    
    return (frequent_patterns, max_count)

