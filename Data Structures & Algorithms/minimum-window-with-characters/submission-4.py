class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ''
        count = {}
        for c in t:
            count[c] = count.get(c, 0) + 1
        l = 0
        match, target = 0, len(count)
        cur_count = {}
        min_len = float('infinity')
        min_pos = [0,0]
        for r, c in enumerate(s):
            if c in count:
                cur_count[c] = cur_count.get(c, 0) + 1
                if cur_count[c] == count[c]:
                    match+=1
            
            while match == target:
                cur_len = r - l + 1
                if cur_len < min_len:
                    min_len = cur_len
                    min_pos = [l, r]
                
                if s[l] in cur_count:
                    if cur_count[s[l]] == count[s[l]]:
                        match-=1
                    cur_count[s[l]] -= 1
                l+=1
        return '' if min_len == float('infinity') else s[min_pos[0]:min_pos[1]+1]