class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        i,j = 0, len(heights) - 1

        while i < j:
            s = (j - i) * min(heights[i], heights[j])
            res = max(res, s)
            if heights[i] < heights[j]:
                i+=1
            else:
                j-=1
        return res