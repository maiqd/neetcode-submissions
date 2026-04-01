class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        for i in range(len(height)):
            l, r = 0, len(height) -1
            maxLeft = maxRight = height[i]
            while l < i:
                maxLeft = max(maxLeft, height[l])
                l+=1
            while r > i:
                maxRight = max(maxRight, height[r])
                r-=1
            cur = min(maxLeft, maxRight) - height[i]
            res+= cur
        return res