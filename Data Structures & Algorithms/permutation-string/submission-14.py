class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        l = 0
        count_s1 = [0] * 26
        for c in s1:
            count_s1[ord(c) - ord("a")] += 1
        curr = [0] * 26

        for r in range(len(s2)):
            if r - l + 1 > len(s1):
                curr[ord(s2[l]) - ord("a")] -= 1
                l += 1

            curr[ord(s2[r]) - ord("a")] += 1
            if curr == count_s1:
                return True
        return False
