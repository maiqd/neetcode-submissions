class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1 = {}
        for s in s1:
            freq1[s] = freq1.get(s, 0) + 1

        l = 0
        freq2 = {}
        lens2 = 0
        print(freq1)
        for r in range(len(s2)):
            freq2[s2[r]] = freq2.get(s2[r],0) + 1
            lens2 +=1
            if lens2 > len(s1):
                freq2[s2[l]] = freq2[s2[l]] - 1
                if freq2[s2[l]] == 0:
                    freq2.pop(s2[l])
                l+=1
            
            if freq1 == freq2:
                return True
            print(freq2)
        return False 


