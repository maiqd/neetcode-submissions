class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        ns = set(nums)
        i = 0
        res = 1
        while i < len(nums):
            num = nums[i]
            if num - 1 in ns:
                i+=1
                continue
            
            length = 1
            while num + length in ns:
                length+=1
                res = max(res, length)
            
            i+=1
        return res