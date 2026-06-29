class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums) * 2):
            key = i
            if key >= len(nums):
                key -= len(nums)
            ans.append(nums[key])

        return ans
