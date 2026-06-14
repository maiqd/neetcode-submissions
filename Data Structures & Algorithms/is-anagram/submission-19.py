class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count1 = [0] * 26
        for i in range(len(s)):
            count1[ord(s[i]) - ord('a')] +=1
            count1[ord(t[i]) - ord('a')] -=1
        for num in count1:
            if num != 0:
                return False
        return True