class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:

        @lru_cache(maxsize=None)
        def getNumberOfPAthsFrom(currPos: int, remStep: int) -> int:
            if not remStep:
                if currPos == endPos:
                    return 1
                return 0
            
            totalNumberOfPaths = 0
            totalNumberOfPaths += getNumberOfPAthsFrom(currPos+1, remStep-1)
            totalNumberOfPaths += getNumberOfPAthsFrom(currPos-1, remStep-1)
            return totalNumberOfPaths
        
        return getNumberOfPAthsFrom(startPos, k) % 1_000_000_007