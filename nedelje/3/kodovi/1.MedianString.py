def median_string(dna, k):
    distance = float('inf')
    median = ''
    
    for i in range(4**k):
        pattern = number_to_pattern(i, k)
        current_distance = d(pattern, dna)
        if distance > current_distance:
            distance = current_distance
            median = pattern
            
    return median