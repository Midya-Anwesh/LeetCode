class Solution:
    def minimumLength(self, s: str) -> int:
        freq = dict()

        for char in s:
            freq[char] = freq.get(char, 0) + 1

        length = 0
        for char in freq:
            if freq[char] < 3:
                length += freq[char]
            elif freq[char] & 1:
                length += 1
            else:
                length += 2
        
        return length