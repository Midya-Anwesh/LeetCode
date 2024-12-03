class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        return " ".join(s[i:j] for i, j in zip([0]+spaces, spaces+[len(s)]))