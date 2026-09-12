class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        longest_freq = 0
        freq = defaultdict(int)
        res = 0
        l = 0
        for r in range(len(s)):
            freq[s[r]] += 1
            longest_freq = max(freq[s[r]], longest_freq)

            while r - l + 1 - longest_freq > k:
                freq[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
