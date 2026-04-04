class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res = False
        count = set()
        for num in nums:
            if num in count:
                return True
            count.add(num)
        return False