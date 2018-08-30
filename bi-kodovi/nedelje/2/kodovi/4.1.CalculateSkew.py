def calculate_skew(text):
    skew = [0 for c in text]
    
    last = 0
    
    for i in range(0,len(text)):
        
        if text[i] == 'g':
            skew[i] = last + 1
            
        elif text[i] == 'c':
            skew[i] = last - 1
            
        else:
            skew[i] = last
            
        last = skew[i]
            
    return skew