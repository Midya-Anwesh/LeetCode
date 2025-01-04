from collections import defaultdict
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # Hash map to store first and last occurence of an alphabet
        indexMap = defaultdict(lambda : [float('inf'), -float('inf')])

        # Fill values in hash map
        for idx, char in enumerate(s):
            indexMap[char][0] = min(idx, indexMap[char][0])
            indexMap[char][1] = max(idx, indexMap[char][1])

        # Return variable
        ans = 0

        # Traverse alphabets in the map
        for char in indexMap:

            # Use a set to keep track of distinct alphabets
            seen = set()

            # Traverse the string from first occurence index + 1 to last occurence index - 1
            for i in range(indexMap[char][0]+1, indexMap[char][1]):
                # Add alphabet to set
                seen.add(s[i])
            # Length of the set will be number of distinct alphabets between first occurence and last occurence index
            # Which is number of distinct/unique length 3 pallindromic sub-sequence that can be formed using that alphabet
            # So, we add it to return variable
            ans += len(seen)

        # Finally return number of unique palindromes of length three
        return ans