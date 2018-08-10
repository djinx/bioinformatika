def probability(pattern, profile):
    prob = 1
    
    for j in range(len(pattern)):
        c = pattern[j]
        index = symbol_to_number(c)
        
        prob *= profile[index][j]
        
    return prob