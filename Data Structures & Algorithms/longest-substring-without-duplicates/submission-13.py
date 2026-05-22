class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        preChar = set()

        l = 0
        res = 0
        for i, c in enumerate(s):
            while c in preChar:
                preChar.remove(s[l])
                l+=1
            preChar.add(c)
            res = max(res, i -l +1)

        return res
