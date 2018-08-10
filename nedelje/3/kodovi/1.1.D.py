def d(pattern, dna):
    k = len(pattern)
    distance = 0
    
    for dna_string in dna:
        h_dist = float('inf')
        
        for i in range(len(dna_string) - k + 1):
            pattern_p = dna_string[i:i+k]
            dist = hamming_distance(pattern_p, pattern)
            
            if dist < h_dist:
                h_dist = dist
                
        distance += h_dist
    return distance