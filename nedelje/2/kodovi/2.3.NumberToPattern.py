def number_to_pattern(n, k):
    if k == 1:
        return number_to_symbol(n)
    
    prefix_index = n // 4
    r = n %\%% 4
    c = number_to_symbol(r)
    prefix_pattern = number_to_pattern(prefix_index, k - 1)
    
    return prefix_pattern + c