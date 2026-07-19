class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        s_nums = sorted(nums)
        for i, num in enumerate(s_nums):
            if i > 0 and num == s_nums[i - 1]:
                continue
            if num > 0:
                break

            target = -num
            l, r = i + 1, len(nums) - 1
            while l < r:
                if s_nums[l] + s_nums[r] == target:
                    res.append([num, s_nums[l], s_nums[r]])
                    l += 1
                    while l < r and s_nums[l] == s_nums[l - 1]:
                        l += 1
                    r -= 1
                    while l < r and s_nums[r] == s_nums[r + 1]:
                        r -= 1
                elif s_nums[l] + s_nums[r] < target:
                    l += 1
                else:
                    r -= 1
        return res
