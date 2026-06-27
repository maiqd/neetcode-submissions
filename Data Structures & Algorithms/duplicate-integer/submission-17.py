class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        preMap = set()

        for num in nums:
            if num in preMap:
                return True
            preMap.add(num)
        return False
