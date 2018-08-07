def neighbors(pattern, d):
    if d == 0: 
        return set([pattern])
    
    if len(pattern) == 1: 
        return set(['a', 't', 'c', 'g'])
    
    neighborhood = set([])
    
    suffix_neighbors = neighbors(pattern[1:], d) 
    
    for text in suffix_neighbors:
        if hamming_distance(pattern[1:], text) < d: 
            for x in ['a','t','c','g']:
                neighborhood.add(x + text) 
        else: 
            neighborhood.add(pattern[0] + text) 
            
    return neighborhood