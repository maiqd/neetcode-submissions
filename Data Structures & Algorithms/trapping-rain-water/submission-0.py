class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        for i in range(len(height)):
            l,r = 0, len(height) - 1
            max_l, max_r = 0, 0
            while l < i:
                max_l = max(max_l, height[l])
                l+=1
            while r > i:
                max_r = max(max_r, height[r])
                r-=1
            water = max(min(max_l, max_r) - height[i], 0)
            print(f'i = {i}, height[i] = {height[i]}, water = {water}, max_l = {max_l}, max_r = {max_r}')
            res += water
        return res