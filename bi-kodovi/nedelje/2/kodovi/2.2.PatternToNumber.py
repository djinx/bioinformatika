def pattern_to_number(pattern):
    if len(pattern) == 0:
        return 0
    
    last = pattern[-1:]
    prefix = pattern[:-1]
    
    return 4 * pattern_to_number(prefix) + symbol_to_number(last)