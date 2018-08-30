def frequent_words(text, k):
    frequent_patterns = set([])
    count = []
    
    for i in range(len(text) - k):
        pattern = text[i:i+k]
        count.append(pattern_count(text, pattern))
        
    max_count = max(count)
    
    for i in range(len(text) - k):
        if count[i] == max_count:
            frequent_patterns.add(text[i:i+k])
    
    return frequent_patterns


