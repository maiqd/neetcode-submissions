class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        longest_repeat = curr_repeat = 0

        for num in nums:
            if num == 1:
                curr_repeat += 1
                longest_repeat = max(curr_repeat, longest_repeat)
            else:
                curr_repeat = 0
        return longest_repeat