class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums) 
        preSum = 1
        for i, num in enumerate(nums):
            res[i] = preSum
            preSum*=num
        postSum = 1
        for i in range(len(nums) -1, -1, -1):
            res[i] *= postSum
            postSum *= nums[i]
        return res