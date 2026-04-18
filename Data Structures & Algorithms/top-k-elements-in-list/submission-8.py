class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums) + 1)]
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        for key, value in count.items():
            bucket[value].append(key)
        print(bucket)
        res = []
        for i in range(len(bucket) -1 , -1, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) >= k:
                    return res
            print(f"{i} : {bucket[i]}")
        return res