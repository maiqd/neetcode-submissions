class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = {}
        maxSeen = 0
        l = 0
        res = 0
        for r, c in enumerate(s):
            seen[c] = seen.get(c,0) + 1
            maxSeen = max(maxSeen, seen[c])
            while r - l + 1 - maxSeen > k:
                seen[s[l]]-=1
                l+=1
            res = max(r-l+1, res)
        return res
