class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        countOfRabbits = dict()
        ret = 0
        for num in answers:
            countOfRabbits[num] = countOfRabbits.get(num, 0) + 1
            if countOfRabbits[num] == num+1:
                countOfRabbits[num] = 0
                ret += num + 1
        for count in countOfRabbits:
            if countOfRabbits[count] > 0:
                ret += count + 1
        return ret