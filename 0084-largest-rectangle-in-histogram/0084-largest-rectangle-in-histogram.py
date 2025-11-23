class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        monoStack = []
        maxArea = 0
        for i in range(len(heights)):
            while len(monoStack) and (heights[monoStack[-1]] > heights[i]):
                currHeight = heights[monoStack.pop()]
                prevSmaller, nextSmaller = monoStack[-1] if len(monoStack) else -1, i
                maxArea = max(maxArea, currHeight * (nextSmaller - prevSmaller - 1))
            monoStack.append(i)
        return maxArea