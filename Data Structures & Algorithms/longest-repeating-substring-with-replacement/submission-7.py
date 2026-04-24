class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        maxFreq = 0
        res = 0
        l = 0
        for r, c in enumerate(s):
            freq[c] = freq.get(c,0) + 1
            maxFreq = max(maxFreq, freq[c])
            while r - l + 1 - maxFreq > k:
                freq[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res