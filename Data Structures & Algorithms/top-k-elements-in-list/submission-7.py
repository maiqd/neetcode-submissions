class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        bucket = [[] for  _ in range(len(nums) + 1)]

        for num, freq in count.items():
            bucket[freq].append(num)
        res = []
        print(bucket)
        for i in range(len(bucket) - 1, -1, -1):
            for p in bucket[i]:
                if len(res) >= k:
                    break
                res.append(p)
        return res