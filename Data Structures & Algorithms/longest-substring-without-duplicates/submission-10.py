class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        res = 0
        l = 0
        for i, c in enumerate(s):
            print(i, c, dic)
            freq = set(s[l:i])
            if c in freq:
                l = dic[c] + 1
            dic[c] = i
            length = i - l +1
            res = max(res, length)
            print(res)
        return res