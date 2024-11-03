class Solution:
    def minimumOperations(self, num: str) -> int:
        def matchEnd(num: str, toMatch: str) -> int:
            ret = len(num)
            for i in range(len(num)-1, -1, -1):
                if num[i] == toMatch[1]:
                    temp, found = len(num)-i-1, False
                    if toMatch == "00":
                        ret = min(ret, temp+i)
                    for j in range(i-1, -1, -1):
                        if num[j] != toMatch[0]:
                            temp += 1
                        else:
                            found = True
                            break
                    if found:
                        return min(ret, temp)
            return min(ret, len(num))
        
        return min(matchEnd(num, "75"), matchEnd(num, "50"), matchEnd(num, "25"), matchEnd(num, "00"))