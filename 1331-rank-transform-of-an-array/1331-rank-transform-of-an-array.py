class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = dict() #To store all ranks of numbers
        last_seen = None #To indicate number we last saw
        for num in sorted(arr): #Traverse the sorted array [don't give a f*** to duplicates]
            if last_seen is None: #if it is the first number that we saw then give least rank
                rank[num] = 1
            elif last_seen != num: #if we see a different number(x) then that number is greater then last seen number
                rank[num] = rank[last_seen]+1 #increase rank of that number(x) by adding 1 with the rank of last seen
            last_seen = num #make the current number as last seen for next iteration

        for num in arr:
            yield rank[num]
