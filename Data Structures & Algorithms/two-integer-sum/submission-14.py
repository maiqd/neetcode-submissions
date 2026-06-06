class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        preMap = {}

        for i in range(len(nums)):
            seen = target - nums[i]
            if seen in preMap:
                return [preMap[seen], i]
            preMap[nums[i]] = i