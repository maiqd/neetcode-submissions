class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consecutive = 0
        curr_consecutive = 0

        for num in nums:
            if num != 1:
                max_consecutive = max(max_consecutive, curr_consecutive)
                curr_consecutive = 0
                continue
            curr_consecutive+=1
        return max(max_consecutive, curr_consecutive)