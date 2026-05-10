class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        snums = sorted(nums)

        res = []
        for i in range(len(nums)):
            if i > 0 and snums[i] == snums[i-1]:
                i+=1
                continue
            num = snums[i]
            if num > 0:
                break;
            target = -num
            
            j = i + 1
            k = len(nums) - 1
            while j < k:
                s = snums[j] + snums[k]

                if s == target:
                    res.append([num, snums[j], snums[k]])
                    while j < k and snums[j] == snums[j+1]:
                        j+=1
                    j+=1
                    while j < k and snums[k] == snums[k-1]:
                        k-=1
                    k-=1
                elif s > target:
                    k-=1
                else:
                    j+=1
                
        return res
