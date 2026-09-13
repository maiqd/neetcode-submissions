class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        res = []
        for index, num in enumerate(sorted_nums):
            if num > 0:
                break
            target = -num

            if index > 0 and sorted_nums[index] == sorted_nums[index - 1]:
                continue

            l, r = index + 1, len(nums) - 1
            while l < r:
                if sorted_nums[l] + sorted_nums[r] == target:
                    res.append([num, sorted_nums[l], sorted_nums[r]])
                    while l < r and sorted_nums[l] == sorted_nums[l + 1]:
                        l += 1
                    while l < r and sorted_nums[r] == sorted_nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif sorted_nums[l] + sorted_nums[r] > target:
                    r -= 1
                else:
                    l += 1

        return res
