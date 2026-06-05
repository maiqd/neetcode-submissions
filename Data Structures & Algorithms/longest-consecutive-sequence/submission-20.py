class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        res = 0
        i = 0
        while i < len(nums):
            num = nums[i]
            if num - 1 in nums_set:
                i+=1
                continue
            length = 1
            while num + length in nums_set:
                length+=1
            res = max(res, length)
            i = i + 1

        return res