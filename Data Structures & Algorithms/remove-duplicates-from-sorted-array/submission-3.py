class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums_set = sorted(set(nums))
        nums[:len(nums_set)] = nums_set
        return len(nums_set)