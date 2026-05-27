class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ''
        count1 = {}
        count2 = {}
        for c in t:
            count1[c] = count1.get(c, 0) + 1
        
        l = 0
        res = float('infinity')
        min_pos = [0, 0]
        matches = 0
        target = len(count1)

        for r, c in enumerate(s):
            if c in count1:
                count2[c] = count2.get(c,0) + 1
                if count1[c] == count2[c]:
                    matches +=1
            while matches == target:
                if s[l] in count1:
                    count2[s[l]]-=1
                    if count2[s[l]] + 1 == count1[s[l]]:
                        matches-=1
                if r - l + 1 <= res:
                    res = r-l+1
                    min_pos = [l, r]
                l+=1
        return '' if res == float('infinity') else s[min_pos[0]: min_pos[1]+1]

