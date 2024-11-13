class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()

        def getIndex(curr: int, st: int, end: int, find_min: int) -> int:
            ret = -1
            while st <= end:
                mid = st+(end-st)//2
                if lower <= nums[curr]+nums[mid] <= upper:
                    if ret == -1:
                        ret = mid
                    if find_min:
                        ret = min(ret, mid)
                        end = mid-1
                    else:
                        ret = max(ret, mid)
                        st = mid+1
                elif nums[curr]+nums[mid] < lower:
                    st = mid+1
                else:
                    end = mid-1
            return ret if ret != -1 else curr
        
        ret = 0
        for i in range(len(nums)):
            min_left, min_right = getIndex(i, 0, i-1, 1), getIndex(i, i+1, len(nums)-1, 1)
            if min_left != i:
                ret += (getIndex(i, 0, i-1, 0) - min_left) + 1
            if min_right != i:
                ret += (getIndex(i, i+1, len(nums)-1, 0) - min_right) + 1
        return ret//2