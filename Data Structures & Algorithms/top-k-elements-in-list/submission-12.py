class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums) + 1)]

        counter_nums = Counter(nums)

        for num, freq in counter_nums.items():
            bucket[freq].append(num)

        res = []

        for i in range(len(nums), 0, -1):
            for num in bucket[i]:
                if len(res) == k:
                    return res
                res.append(num)
        return res
