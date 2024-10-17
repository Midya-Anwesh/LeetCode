class Solution:
    def maximumSwap(self, num: int) -> int:
        num, best = list(str(num)), sorted(str(num), reverse = True)
        for i in range(len(best)):
            if num[i] != best[i]:
                index = None
                for j in range(len(num)-1, -1, -1):
                    if num[j] == best[i]:
                        index = j
                        break
                num[i], num[j] = num[j], num[i]
                break
        return int("".join(num))