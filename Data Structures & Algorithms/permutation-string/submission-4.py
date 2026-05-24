class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1Freq = [0] * 26 
        s2WindowFreq = [0] * 26
        for c in s1:
            s1Freq[ord(c) - ord('a')] += 1
        
        l = 0
        for r, c in enumerate(s2):
            while r - l + 1 > len(s1):
                s2WindowFreq[ord(s2[l]) - ord('a')]-=1
                l+=1
            s2WindowFreq[ord(s2[r]) - ord('a')]+=1
            if s1Freq == s2WindowFreq:
                return True
        return False
