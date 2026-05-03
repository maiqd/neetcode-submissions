class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = [[] for _ in range(len(nums) + 1)]
        res = []
        count = {}
        for num in nums:
            count[num] = count.get(num,0) + 1
        
        for key,value in count.items():
            arr[value].append(key)
        
        for i in range(len(nums), 0, -1):
            for j in arr[i]:
                if len(res)>= k:
                    return res
                res.append(j)
        return res