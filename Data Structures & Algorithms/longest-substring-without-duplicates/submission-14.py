class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = set()
        l = 0
        res = 0
        for r,c in enumerate(s):
            while c in count:
                count.remove(s[l])
                l+=1
            count.add(c)
            res = max(res, r-l+1)
        return res