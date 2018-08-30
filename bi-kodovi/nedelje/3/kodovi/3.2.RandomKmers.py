def random_k_mers(dna, k, t):
    k_mers = []
    
    for i in range(t):
        start = random.randrange(0, len(dna[i]) - k + 1)
        dna_string = dna[i]
        k_mers.append(dna_string[start:start+k])

    return k_mers