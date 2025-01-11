class Solution:
    def canConstruct(self, s: str, k: int) -> bool:


        """
        
        if (number of character having odd count>k) return false;
        
        """


        if len(s) < k:
            return False
        if len(s) == k:
            return True

        chars = dict()
        for char in s:
            chars[char] = chars.get(char, 0) + 1
        
        odd_count = 0
        for char in chars:
            odd_count += chars[char]&1

        return odd_count <= k
                    