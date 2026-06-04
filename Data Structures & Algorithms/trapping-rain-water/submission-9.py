class Solution:
    def trap(self, height: List[int]) -> int:
        
        l,r = 0, len(height) - 1
        maxLeft = height[l]
        maxRight = height[r]
        res = 0
        while l < r:
            if maxLeft < maxRight:
                l+=1
                maxLeft = max(maxLeft, height[l])
                water = max(min(maxLeft, maxRight) - height[l], 0)
                res+= water
            else:
                r-=1
                maxRight = max(maxRight, height[r])
                water = max(min(maxRight, maxLeft) - height[r], 0)
                res += water
        return res