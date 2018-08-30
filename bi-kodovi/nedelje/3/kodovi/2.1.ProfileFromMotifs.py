def profile_from_motifs(motifs, k, t):
    profile = [[1 for i in range(k)] for x in range(4)]
    
    for j in range(k):
        for i in range(t):
            index = symbol_to_number(motifs[i][j])
            profile[index][j] += 1
            
    for j in range(k):
        for i in range(4):
            profile[i][j] /= (t+2)
            
    return profile