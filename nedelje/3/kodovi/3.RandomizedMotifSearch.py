import copy

def randomized_motif_search(dna, k, t):

    motifs = random_k_mers(dna, k, t)
    best_motifs = copy.deepcopy(motifs)
    best_score = score(best_motifs, k)

    while True:
        profile = profile_from_motifs(motifs, k, t)
        motifs = motifs_from_profile(profile, dna)
        current_score = score(motifs, k)
        
        if current_score < best_score:
            best_score = current_score
            best_motifs = copy.deepcopy(motifs)
        else:
            return best_motifs