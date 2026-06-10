class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min_len = float('inf')
        min_pos = [0,0]
        if len(s) < len(t):
            return ''
        count_t = {}
        count_s = {}
        for i in range(len(t)):
            count_t[t[i]] = count_t.get(t[i],0) + 1
        print(count_t)
        target = len(count_t)
        matches = 0
        l = 0
        for r, c in enumerate(s):
            if c in count_t:
                count_s[c] = count_s.get(c,0) + 1
                if count_s[c] == count_t[c]:
                    matches+=1
                while matches == target:
                    if r-l+1 < min_len:
                        min_len = r-l+1
                        min_pos = [l, r]
                    if s[l] in count_t:
                        count_s[s[l]] -=1
                        if count_s[s[l]] + 1 == count_t[s[l]]:
                            matches -=1
                    l+=1

        return '' if min_len == float('inf') else s[min_pos[0]:min_pos[1]+1]