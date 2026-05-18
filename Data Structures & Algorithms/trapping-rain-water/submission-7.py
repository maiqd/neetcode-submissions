class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1
        maxLeft, maxRight = height[l], height[r]

        while l < r:
            if maxLeft < maxRight:
                l+=1
                maxLeft = max(height[l], maxLeft)
                area = max(0, min(maxLeft, maxRight) - height[l])
                res += area
            else:
                r-=1
                maxRight = max(height[r], maxRight)
                area = max(0, min(maxLeft, maxRight) - height[r])
                res+= area

        return res