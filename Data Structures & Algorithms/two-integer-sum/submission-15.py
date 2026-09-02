class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pre = {}

        for  i, num in enumerate(nums):
            seen = target - num
            if seen in pre:
                return [pre[seen], i]
            pre[num] = i
        return []