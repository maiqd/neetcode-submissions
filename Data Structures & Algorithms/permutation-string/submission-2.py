class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = [0] * 26
        count2 = [0] * 26
        for s in s1:
            count1[ord(s) - ord('a')] +=1

        l = 0
        lens2 = 0
        for r in s2:
            count2[ord(r) - ord('a')] += 1
            lens2 +=1
            if lens2 > len(s1):
                count2[ord(s2[l]) - ord('a')] -=1
                l+=1
            
            if count1 == count2:
                return True
        return False 


