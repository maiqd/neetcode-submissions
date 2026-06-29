class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxRepeat = 0
        count = 0

        for num in nums:
            if num != 1:
                count = 0
            else:
                count += 1
                maxRepeat = max(maxRepeat, count)
        return maxRepeat
