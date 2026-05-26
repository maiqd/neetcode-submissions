class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1 = [0] * 26
        freq2 = [0] * 26
        for c in s1:
            index = ord(c) - ord('a')
            freq1[index] += 1
        l = 0
        for r, c in enumerate(s2):
            if freq1 == freq2:
                return True
            while r - l + 1 > len(s1):
                freq2[ord(s2[l]) - ord('a')] -=1
                l+=1
            freq2[ord(c) - ord('a')] +=1
        return freq1 == freq2
