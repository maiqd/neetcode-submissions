class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        len_nums = len(nums)
        ans = [0 for _ in range(len_nums * 2)]

        for i in range(len(ans)):
            index = i if i < len_nums else i - len_nums
            ans[i] = nums[index]
        return ans
