from heapq import heappush, heappop

class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        """
        Replacement policy,
            1. Charecters on odd indices can be swapped with characters on odd indices
            2. Characters on even indices can be swapped with characters on even indices
        As even-even = even and odd-odd = even
        """
        s1 = list(s1)
        # 0 -> even, 1 -> odd
        # Create a map which
        #   1. Separetes all charecter of s1 in two buckets [odd(1), even(0)]
        #   2. Holds heap of all indices where current character occures
        evenOddMap = defaultdict(
            lambda: defaultdict(list)
        )
        # Fill the map
        for idx, char in enumerate(s1):
            heappush(evenOddMap[idx&1][char], idx)
        
        # Now, check if s1 can be converted to s2
        for idx, char in enumerate(s1):
            # If current character in s1 and s2 does not match
            if char != s2[idx]:
                # Check if we have that required character in s1 
                # Check if we can replace it with required character
                if len(evenOddMap[idx&1][s2[idx]]) <= 0:
                    # If not return false
                    return False
                else:
                    # Otherwise swap the characters in s1, and update the map
                    i = heappop(evenOddMap[idx&1][s2[idx]])
                    heappop(evenOddMap[idx&1][char])
                    s1[idx], s1[i] = s1[i], char
                    heappush(evenOddMap[idx&1][char], i)
            # If current character matches to s2 just remove current index from heap
            else:
                heappop(evenOddMap[idx&1][char])
        
        # If all iterations done, return true
        return True
