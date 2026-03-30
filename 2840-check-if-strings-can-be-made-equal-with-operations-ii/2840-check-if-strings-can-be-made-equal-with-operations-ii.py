from heapq import heappush, heappop

class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        s1 = list(s1)
        # 0 -> even, 1 -> odd
        # Create a map which specifies which chars are present in odd and even indices and how many
        evenOddMap = defaultdict(
            lambda: defaultdict(list)
        )
        for idx, char in enumerate(s1):
            heappush(evenOddMap[idx&1][char], idx)
        
        # Now, check if s1 can be converted to s2
        for idx, char in enumerate(s1):
            if char != s2[idx]:
                if len(evenOddMap[idx&1][s2[idx]]) <= 0:
                    return False
                else:
                    i = heappop(evenOddMap[idx&1][s2[idx]])
                    heappop(evenOddMap[idx&1][char])
                    s1[idx], s1[i] = s1[i], char
                    heappush(evenOddMap[idx&1][char], i)
            else:
                heappop(evenOddMap[idx&1][char])
        
        return True
