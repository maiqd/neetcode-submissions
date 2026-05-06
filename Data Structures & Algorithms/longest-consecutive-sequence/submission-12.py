class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        sorted_nums = sorted(nums)
        res = 1
        cur_len = 1
        for i in range(1, len(sorted_nums), 1):
            if sorted_nums[i] == sorted_nums[i-1]:
                continue
            elif sorted_nums[i] == sorted_nums[i-1] + 1:
                cur_len += 1
            else:
                cur_len = 1
            res = max(res, cur_len)

        return res