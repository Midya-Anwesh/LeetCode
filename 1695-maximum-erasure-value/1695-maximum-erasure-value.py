class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        maxSum = nums[0]
        lastSeen = dict()
        winSt = 0
        for i in range(len(nums)):
            winSt = max(winSt, lastSeen.get(nums[i], -1) + 1)
            maxSum = max(maxSum, prefix[i+1] - prefix[winSt])
            lastSeen[nums[i]] = i
        return maxSum