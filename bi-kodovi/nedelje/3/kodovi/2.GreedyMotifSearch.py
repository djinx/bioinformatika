def greedy_motif_search(dna, k, t):
    best_motifs = [dna_string[0:k] for dna_string in dna]
    best_score = score(best_motifs, k)
    first_string = dna[0]
    
    for i in range(len(first_string) - k): 
        motifs = []
        motifs.append(first_string[i:i+k])

        for j in range(1, t):
            profile = profile_from_motifs(motifs, k, j)
            motifs.append(most_probable_k_mer(dna[j], profile, k))
            
        current_score = score(motifs, k)
        
        if current_score < best_score:
            best_motifs = copy.deepcopy(motifs)
            best_score = current_score
        
    return best_motifs