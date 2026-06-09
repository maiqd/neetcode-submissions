class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        count1 = [0] * 26
        count2 = [0] * 26
        matches = 0
        for i in range(len(s1)):
            count1[ord(s1[i])-ord('a')] += 1
            count2[ord(s2[i])-ord('a')] += 1
        for i in range(len(count1)):
            if count1[i] == count2[i]:
                matches += 1
        l = 0
        for i in range(len(s1), len(s2), 1):
            if matches == 26:
                return True
            key = ord(s2[i]) - ord('a')
            count2[key] +=1
            if count1[key] == count2[key]:
                matches+=1
            elif count1[key] == count2[key] - 1:
                matches-=1

            key = ord(s2[l]) - ord('a')
            count2[key] -=1
            if count1[key] == count2[key]:
                matches+=1
            elif count1[key] == count2[key]+1:
                matches-=1
            l+=1

        return matches == 26