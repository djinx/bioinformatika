# Prevodjenje brojeva u nukleotide        
def number_to_symbol(n):
    pairs = {
        0 : 'a',
        1 : 't',
        2 : 'c',
        3 : 'g'
    }
    
    return pairs[n]