def motifs_from_profile(profile, dna):
    motifs = []
    k = len(profile[0])
    
    for dna_string in dna:
        motifs.append(most_probable_k_mer(dna_string, profile, k))

    return motifs