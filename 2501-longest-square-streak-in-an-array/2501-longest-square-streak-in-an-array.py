class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums = {num:1 for num in nums}
        ret = -1

        def bfs(num: int) -> int:
            length_of_streak = 0
            nums[num] = 0
            queue = [num]
            while len(queue):
                length_of_streak += 1
                curr = queue.pop(0)
                if ((curr_sqrt:=curr**(1/2)) in nums) and nums[curr_sqrt]:
                    queue.append(curr_sqrt)
                    nums[curr_sqrt] = 0
                if ((curr_sqr:=curr*curr) in nums) and nums[curr_sqr]:
                    queue.append(curr_sqr)
                    nums[curr_sqr] = 0
            return length_of_streak

        for num in nums:
            if nums[num]:
                len_of_longest = -1 if (l:=bfs(num)) <= 1 else l
                ret = max(ret, len_of_longest)

        return ret