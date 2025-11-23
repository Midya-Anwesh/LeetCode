class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        prevSmallIndices, nextSmallIndices = [-1 for _ in range(len(heights))], [len(heights) for _ in range(len(heights))]
        maxStack, minStack = [], []
        for i in range(len(heights)):
            while len(maxStack) and heights[maxStack[-1]] >= heights[i]:
                maxStack.pop()
            if len(maxStack):
                prevSmallIndices[i] = maxStack[-1]

            while len(minStack) and heights[minStack[-1]] > heights[i]:
                nextSmallIndices[minStack.pop()] = i
            
            minStack.append(i)
            maxStack.append(i)
        return max(heights[i] * (nextSmallIndices[i]-prevSmallIndices[i]-1) for i in range(len(heights)))