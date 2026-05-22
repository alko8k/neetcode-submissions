class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0 
        l = 0
        r = len(heights) - 1
        while l < r:
            h = min(heights[l], heights[r])
            area = max(area, h * (r - l))

            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                r-=1
                l+=1
        return area
        