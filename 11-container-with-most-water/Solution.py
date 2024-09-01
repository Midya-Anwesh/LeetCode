# runtime = 525.0ms
# memory usage = 29.8MB

class Solution:

    def maxArea(self, height: list[int]) -> int:

        ret,start,end = 0,0,len(height)-1

        while(start < end):

            a = min(height[start],height[end])*(end-start)

            ret = max(ret,a)

            if height[start] < height[end]:

                start += 1

            else:

                end -= 1

        return ret

        