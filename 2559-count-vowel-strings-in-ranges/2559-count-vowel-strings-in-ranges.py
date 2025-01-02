VOWELS = "aeiou"
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        # Let us assume words starting and ending with vowels are good words
        # Prefix sum of each index in words
        # prefix[i] represents number of good words before index i of words
        # e.g: prefix[1] = 1, means there is 1 good word before inedex 1 of words
        prefix = [0] * (len(words)+1)
        
        # Fill the prefix sum
        for i in range(1, len(prefix)):
            prefix[i] = prefix[i-1] + (words[i-1][0] in VOWELS and words[i-1][-1] in VOWELS)
        
        # ans vector
        ans = []
        # Iterate over the queries
        for l, r in queries:

            # The number of words starting and ending with a vowel within the index l to r inclusive can be calculated as
            # (Number of good words before index r) + (1 if r is good word) - (Number of good string before index l)

            ans.append(prefix[r] + (words[r][0] in VOWELS and words[r][-1] in VOWELS) - prefix[l])
        
        # Return ans vector
        return ans