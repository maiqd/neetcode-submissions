class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1
        maxLeft, maxRight = height[l], height[r]

        while l < r:
            maxLeft = max(maxLeft, height[l])
            maxRight = max(maxRight, height[r])

            if height[l] < height[r]:
                cur = min(maxLeft, maxRight) - height[l]
                res+= cur
                l+=1
            else:
                cur = min(maxLeft, maxRight) - height[r]
                res+= cur
                r-=1

        return res