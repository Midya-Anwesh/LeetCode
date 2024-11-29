class Solution:
    def check(self, nums: List[int]) -> bool:
        st_element = min(nums)
        indices = [i for i in range(len(nums)) if nums[i] == st_element]
        isSorted = True

        for index in indices:
            st, end = index, (index+1)%len(nums)
            isSorted = True
            while st != end:
                if nums[ (len(nums)+end-1)%len(nums) ] > nums[end]:
                    isSorted = False
                    break
                end = (end+1)%len(nums)
            if isSorted:
                break

        return isSorted