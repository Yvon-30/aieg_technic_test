def longest_unique_substring(s):
    char_set = {}
    start = 0 
    max_length = 0

    for end in range(len(s)):
        if s[end] in char_set and char_set[s[end]] >= start:
            start = char_set[s[end]] + 1
        
        char_set[s[end]] = end
        
        max_length = max(max_length, end - start + 1)

    return max_length