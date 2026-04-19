class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s_nums = sorted(nums)
        res = []
        for i in range(len(nums)):
            if i > 0 and s_nums[i] == s_nums[i-1]:
                continue
            target = 0 - s_nums[i]
            l, r = i+1, len(nums) - 1
            while l < r:
                s = s_nums[l] + s_nums[r]
                if s == target:
                    res.append([s_nums[i],s_nums[l],s_nums[r]])
                    while l < r and s_nums[l] == s_nums[l+1]:
                        l+=1
                    l+=1
                    while l < r and s_nums[r] == s_nums[r-1]:
                        r-=1
                    r-=1
                elif s < target:
                    l+=1
                else:
                    r-=1
        return res
