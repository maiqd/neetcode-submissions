class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        count1 = [0] * 26
        for c in s1:
            count1[ord(c)- ord('a')] += 1        
        
        seen = [0] * 26
        l = 0
        for r, c in enumerate(s2):
            seen[ord(c)- ord('a')] += 1
            print(seen, count1)
            if seen == count1:
                return True
            
            while r - l + 1 >= len(s1):
                seen[ord(s2[l])- ord('a')] -= 1
                l+=1
            
        return seen == count1