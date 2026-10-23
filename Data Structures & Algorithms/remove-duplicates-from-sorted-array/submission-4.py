class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = r = 0
        while r < len(nums):
            if nums[l] == nums[r]:
                r += 1
                continue
            l += 1
            nums[l] = nums[r]
        return l + 1
