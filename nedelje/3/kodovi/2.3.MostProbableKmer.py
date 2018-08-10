def most_probable_k_mer(dna_string, profile, k):
    
    best_k_mer = ''
    best_probability = -1
    
    for i in range(len(dna_string) - k + 1):
        pattern = dna_string[i:i+k]
        pattern_prob = probability(pattern, profile)
        
        if pattern_prob > best_probability:
            best_probability = pattern_prob
            best_k_mer = pattern
            
    return best_k_mer