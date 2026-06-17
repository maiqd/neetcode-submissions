class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        maxFreq = 0
        curFreq = defaultdict(int)
        res = 0
        for r, c in enumerate(s):
            curFreq[c] += 1
            maxFreq = max(maxFreq, curFreq[c])

            while r - l + 1 - maxFreq > k:
                curFreq[s[l]] -= 1
                l+=1
            res = max(res, r - l + 1)
        return res