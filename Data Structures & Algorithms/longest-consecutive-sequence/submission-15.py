class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        num_set = set(nums)
        res = 1
        i = 0
        while i < len(nums):
            num = nums[i]
            if num - 1 in num_set:
                i+=1
                continue
            
            length = 1
            while num + length in num_set:
                length +=1
                res = max(length, res)
            i+=1
        return res