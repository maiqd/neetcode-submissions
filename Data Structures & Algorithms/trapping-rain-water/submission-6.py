class Solution:
    def trap(self, height: List[int]) -> int:
        
        l,r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]
        area = 0
        while l < r:
            if maxL < maxR:
                l+=1
                maxL = max(maxL, height[l])
                cur = max(0, min(maxL, maxR) - height[l])
                area += cur
            else:
                r-=1
                maxR = max(maxR, height[r])
                cur = max(0, min(maxR, maxL) - height[r])
                area += cur
        return area