class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        """
        Credit -> https://leetcode.com/problems/make-array-elements-equal-to-zero/description/comments/2785957/
        Intuition....
        sum_left --> sum of all elements in left to nums[i]
        sum_right --> sum of all elements in right to nums[i]
        when nums[i] ==0 and sum_right == sum_left : count+=2
        when nums[i] ==0 and sum_right-1==sum_left : count +=1
        when nums[i] == 0 and sum_right == sum_left-1 : count +=1
        """
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)

        totalWays = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                if prefix[i] == prefix[-1] - prefix[i]:
                    totalWays += 2
                elif (prefix[-1] - prefix[i] -1 == prefix[i]) or (prefix[i]-1 == prefix[-1] - prefix[i]):
                    totalWays += 1
        return totalWays