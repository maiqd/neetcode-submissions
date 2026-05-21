class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        l = 0
        curMax = 0
        res = 0
        for r, c in enumerate(s):
            count[ord(c) - ord('A')] +=1
            curMax = max(curMax, count[ord(c) - ord('A')])
            while r - l + 1 - curMax > k:
                count[ord(s[l]) - ord('A')]-=1
                l+=1
            res = max(res, r-l+1)
        return res
