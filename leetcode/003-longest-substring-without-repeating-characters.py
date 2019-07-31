#!/usr/bin/env ipython3

def get_longest_substring_length(s: str) -> int:
    d = {}
    # inital start and length is 0
    start = 0
    length = 0

    for i,char in enumerate(s):
        # repeating char
        if char in d:
            # take max of start and current ind
            start = max(start, d[char] + 1)
        # new char
        else:
            d[char] = i
            length = max(length, i - start + 1)

    return length


strings = ["abcabcbb","dvdf", "ckilbkd", "pwwkew", "bbbbbbbbb"]

for string in strings:
    output = get_longest_substring_length(string)
    print(string, ":" , output) 

