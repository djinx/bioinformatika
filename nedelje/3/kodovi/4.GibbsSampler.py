# Pronalazenje skupa motiva nakon N iteracija koriscenjem Gibs sampler-a
def gibbs_sampler(dna, k, t, N):
    motifs = random_k_mers(dna, k, t)
    best_motifs = copy.deepcopy(motifs)
    best_score = score(best_motifs, k)
    
    for j in range(N):
        i = random.randrange(0,t)
        
        selected_motifs = copy.deepcopy(motifs)
        del selected_motifs[i]
        
        profile = profile_from_motifs(selected_motifs, k, t-1)
        
        motifs[i] = most_probable_k_mer(dna[i], profile, k)
        del selected_motifs
        
        current_score = score(motifs, k)
        
        if current_score < best_score:
            best_motifs = copy.deepcopy(motifs)
            best_score = current_score
            
    return best_motifs
