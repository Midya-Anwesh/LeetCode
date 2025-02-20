class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        length = len(nums[0])
        nums = {num: "STR" for num in nums}

        def getUnique(s: str) -> str:
            if len(s) == length:
                if not (s in nums):
                    return s
                return ""
            
            ret = ""
            for char in ("0", "1"):
                ret = getUnique(s+char)
                if ret != "":
                    return ret
            return ""
        
        return getUnique("")