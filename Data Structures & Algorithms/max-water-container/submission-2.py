class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights) - 1
        maxW = 0
        while l<r:
            water = min(heights[l],heights[r]) * (r - l)
            maxW = max(water, maxW)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return maxW