class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums_set = set(nums)
        res = 0
        for i in range(len(nums)):
            if nums[i] - 1 in nums_set:
                continue

            length = 1
            while nums[i] + length in nums_set:
                length += 1
            res = max(length, res)
        return res
