def hamming_distance(text1, text2):
    distance = 0
    
    for i in range(len(text1)):
        if text1[i] != text2[i]:
            distance += 1
    return distance