class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = []
        
        i = 0

        while i < len(nums):

            remaining = -nums[i]
            st, end = i+1, len(nums)-1
            while st < end:
                if nums[st]+nums[end] < remaining:
                    st += 1
                    # Take the start where distinct element is
                    while st < end and nums[st] == nums[st-1]:
                        st += 1
                elif nums[st]+nums[end] > remaining:
                    end -= 1
                    # Take the end where distinct element is
                    while end > st and nums[end] == nums[end+1]:
                        end -= 1
                else:
                    ret.append([nums[i], nums[st], nums[end]])
                    st, end = st+1, end-1
                    # Adjust start and end
                    while st < end and nums[st] == nums[st-1]:
                        st += 1
                    while end > st and nums[end] == nums[end+1]:
                        end -= 1

            i += 1
            while i < len(nums) and nums[i] == nums[i-1]:
                i += 1
        
        return ret