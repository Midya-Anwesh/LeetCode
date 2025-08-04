class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        typeslastSeen = dict()
        maxLen, win_st = 1, 0
        for i in range(len(fruits)):
            if fruits[i] not in typeslastSeen:
                if len(typeslastSeen) == 2:
                    maxLen = max(maxLen, i - win_st)
                    type1, type2 = typeslastSeen.keys()
                    if typeslastSeen[type1] < typeslastSeen[type2]:
                        win_st = typeslastSeen[type1] + 1
                        typeslastSeen.pop(type1)
                    else:
                        win_st = typeslastSeen[type2] + 1
                        typeslastSeen.pop(type2)
            typeslastSeen[fruits[i]] = i
            maxLen = max(maxLen, i - win_st + 1)
        return maxLen