class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        count = [0] * 26
        curr = [0] * 26

        for c in s1:
            count[ord(c) - ord("a")] += 1

        l = 0
        for r in range(len(s2)):
            curr[ord(s2[r]) - ord("a")] += 1

            while r - l + 1 > len(s1):
                curr[ord(s2[l]) - ord("a")] -= 1
                l += 1
                
            if curr == count:
                return True

        return False
