class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = 0
        most_repeat = 0
        count = defaultdict(int)
        res = 0
        for r in range(len(s)):
            count[s[r]] += 1
            most_repeat = max(most_repeat, count[s[r]])

            while l < r and r - l + 1 - most_repeat > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
