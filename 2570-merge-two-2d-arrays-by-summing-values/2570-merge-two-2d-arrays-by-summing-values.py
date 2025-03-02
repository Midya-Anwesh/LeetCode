class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        num1Index, num2Index = 0, 0
        ret = []

        while (num1Index < len(nums1)) and (num2Index < len(nums2)):
            if nums1[num1Index][0] == nums2[num2Index][0]:
                ret.append([ nums1[num1Index][0], nums1[num1Index][1] + nums2[num2Index][1] ])
                num1Index += 1
                num2Index += 1

            elif nums1[num1Index][0] < nums2[num2Index][0]:
                ret.append(nums1[num1Index])
                num1Index += 1

            else:
                ret.append(nums2[num2Index])
                num2Index +=1
        
        while num1Index < len(nums1):
            ret.append(nums1[num1Index])
            num1Index += 1
        while num2Index < len(nums2):
            ret.append(nums2[num2Index])
            num2Index += 1
        
        return ret