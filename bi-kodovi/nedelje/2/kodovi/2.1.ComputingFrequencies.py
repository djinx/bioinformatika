def computing_frequencies(text, k):
    frequency_array = [0 for i in range(4**k)]
    
    for i in range(len(text) - k):
        pattern = text[i:i+k]
        j = pattern_to_number(pattern)
        frequency_array[j] += 1
    
    return frequency_array