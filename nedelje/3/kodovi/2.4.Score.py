# Izracunavanje ukupnog skora za skup motiva
def score(motifs, k):
    t = len(motifs)
    
    total_score = 0
    
    for j in range(k):
        
        counts = [0, 0, 0, 0]
        
        for i in range(t):
            c = motifs[i][j]
            index = symbol_to_number(c)
            counts[index] += 1
            
        max_index = 0
        
        for i in range(1,4):
            if counts[i] > counts[max_index]:
                max_index = i
                
        total_score += t - counts[max_index]
        
    return total_score