class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        def checkInc(idx: int) -> int:
            while idx < len(nums)-1:
                if nums[idx+1] == nums[idx]:
                    return -1
                elif nums[idx+1] > nums[idx]:
                    idx += 1
                else:
                    break
            return idx
        
        def checkDec(idx: int) -> int:
            while idx < len(nums)-1:
                if nums[idx+1] == nums[idx]:
                    return -1
                elif nums[idx+1] < nums[idx]:
                    idx += 1
                else:
                    break
            return idx
        
        p = checkInc(0)
        if p >= len(nums) or p == -1 or p == 0:
            return False
        q = checkDec(p)
        if q >= len(nums)-1 or q == -1 or p == q:
            return False
        r = checkInc(q)
        if r < len(nums)-1 or r == -1 or q == r:
            return False
        return True