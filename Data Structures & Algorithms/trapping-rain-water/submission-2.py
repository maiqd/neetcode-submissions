class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        maxLeft = height[0]
        for i in range(len(height)):
            r = len(height) -1
            maxRight = height[i]
            while r > i:
                maxRight = max(maxRight, height[r])
                r-=1
            maxLeft = max(maxLeft, height[i])
            cur = min(maxLeft, maxRight) - height[i]
            res+= cur
        return res