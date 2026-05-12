class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        sorted_nums = sorted(nums)
        for i, num in enumerate(sorted_nums):
            if num > 0:
                break
            if i > 0 and sorted_nums[i] == sorted_nums[i-1]:
                continue
            target = -num
            j,k = i+1, len(sorted_nums) -1
            while j < k:
                sum_num = sorted_nums[j] + sorted_nums[k]
                if sum_num == target:
                    res.append([num, sorted_nums[j], sorted_nums[k]])
                    while j < k and sorted_nums[j] == sorted_nums[j+1]:
                        j+=1
                    while j < k and sorted_nums[k] == sorted_nums[k-1]:
                        k-=1
                    j+=1
                    k-=1
                elif sum_num > target:
                    k-=1
                else:
                    j+=1

        return res