class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count, countOfCount = dict(), dict()
        for num in arr:
            if num in count:
                countOfCount[count[num]] -= 1
                count[num] += 1
            else:
                count[num] = 1
            countOfCount[count[num]] = countOfCount.get(count[num], 0) + 1
        
        for Count in countOfCount:
            if countOfCount[Count] > 1:
                return False
        
        return True