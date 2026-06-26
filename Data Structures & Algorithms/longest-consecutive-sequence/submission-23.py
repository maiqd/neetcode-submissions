class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums_set = set(nums)
        res = 1
        for num in nums:
            if num - 1 in nums_set:
                continue

            length = 1
            while num + length in nums_set:
                res = max(res, length + 1)
                length += 1
        return res
