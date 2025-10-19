class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        prevGen = set()
        def dfs(s: str) -> str:
            sAdd = "".join( str((int(s[i])+a)%10) if i&1 else s[i] for i in range(len(s)) )
            if sAdd not in prevGen:
                prevGen.add(sAdd)
                sAdd = dfs(sAdd)
            sRotate = s[-b:] + s[:-b]
            if sRotate not in prevGen:
                prevGen.add(sRotate)
                sRotate = dfs(sRotate)
            return min(sAdd, sRotate)
        return dfs(s)