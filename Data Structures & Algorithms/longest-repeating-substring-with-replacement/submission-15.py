class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count = defaultdict(int)
        longest_count = 0
        res = 0
        for r in range(len(s)):
            count[s[r]] += 1
            longest_count = max(longest_count, count[s[r]])
            while l < r and r - l + 1 - longest_count > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
