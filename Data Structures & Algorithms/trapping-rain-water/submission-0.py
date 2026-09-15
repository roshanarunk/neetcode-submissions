class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        prefix = [0] * len(height)
        suffix = [0] * len(height)
        maxL = 0
        for i,x in enumerate(height):
            prefix[i] = maxL
            maxL = max(maxL, x)
        maxR = 0
        for i in range(len(height) - 1, -1, -1):
            x = height[i]
            suffix[i] = maxR
            maxR = max(maxR, x)
        
        for i,x in enumerate(height):
            minH = min(suffix[i], prefix[i])
            if x < minH:
                total += minH-x
        return total


        
            