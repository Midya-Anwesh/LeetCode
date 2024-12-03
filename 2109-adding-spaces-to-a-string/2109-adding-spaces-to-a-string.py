class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        spaces = set(spaces)
        return "".join([" "+s[i] if i in spaces else s[i] for i in range(len(s))])