class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        s: int = 0
        for i in range(len(chalk)):
            if (k-s) < chalk[i]:
                return i
            s += chalk[i]

        k, s, ret = k%s, 0, -1

        for i in range(len(chalk)):
            if (k-s) < chalk[i]:
                ret = i
                break
            s += chalk[i]

        return ret
        