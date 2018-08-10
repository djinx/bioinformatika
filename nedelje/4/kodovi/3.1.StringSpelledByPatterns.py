# Sastavljanje DNK niske pomocu k-mera
def string_spelled_by_patterns(patterns, k):
    dna_string = patterns[0][:-1]

    for i in range(0, len(patterns)):
        dna_string += patterns[i][-1]

    return dna_string