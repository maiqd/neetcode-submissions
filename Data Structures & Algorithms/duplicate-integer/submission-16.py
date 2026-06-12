class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        pre = set()
        for num in nums:
            if num in pre:
                return True
            pre.add(num)

        return False