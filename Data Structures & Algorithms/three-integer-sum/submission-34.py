class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        s_nums = sorted(nums)
        for i, num in enumerate(s_nums):
            if num > 0:
                break
            if i > 0 and s_nums[i] == s_nums[i-1]:
                continue
            target = -num
            j, k = i + 1, len(s_nums)-1
            while j < k:
                s = s_nums[j] + s_nums[k]
                if s == target:
                    res.append([num, s_nums[j], s_nums[k]])
                    while j < k and s_nums[j] == s_nums[j+1]:
                        j+=1 
                    j+=1
                    while j < k and s_nums[k] == s_nums[k-1]:
                        k-=1
                    k-=1
                elif s > target:
                    k-=1
                else:
                    j+=1

        return res