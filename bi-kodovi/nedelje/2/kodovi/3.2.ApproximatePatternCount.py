def approximate_pattern_count(text, pattern, d):
    count = 0
    
    for i in range(len(text) - len(pattern)):
        pattern_p = text[i:i+len(pattern)]
        
        if hamming_distance(pattern, pattern_p) <= d:
            count += 1
            
    return count