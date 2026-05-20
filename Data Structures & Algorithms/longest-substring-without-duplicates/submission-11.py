class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = set()
        res = 0
        l = 0
        for i, c in enumerate(s):
            while c in freq:
                freq.remove(s[l])
                l+=1
            freq.add(c)
            res = max(res, i-l+1)
        return res