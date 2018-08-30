def frequent_words_with_mismatches(text, k, d):
    frequent_patterns = set([])
    close = [0 for i in range(4**k)]
    frequency_array = [0 for i in range(4**k)] 
    
    for i in range(len(text) - k):
        neighborhood = neighbors(text[i:i+k], d)
        
        for pattern in neighborhood:
            index = pattern_to_number(pattern) 
            close[index] = 1 
            
    for i in range(4**k):
        if close[i] == 1:
            pattern = number_to_pattern(i, k)
            frequency_array[i] = approximate_pattern_count(text, 
                                                         pattern, d)
    max_count = max(frequency_array)
    
    for i in range(4**k):
        if frequency_array[i] == max_count:
            pattern = number_to_pattern(i, k)
            frequent_patterns.add(pattern)
    
    return frequent_patterns
    