class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ''
        count = {}
        for c in t:
            count[c] = count.get(c, 0) + 1
        
        cur_freq = {}
        match = 0
        expect = len(count)
        l=0
        min_len = float('infinity')
        min_pos = [0,0]
        print(count)
        for r, c in enumerate(s):
            if c in count:
                cur_freq[c] = cur_freq.get(c, 0) + 1
                if cur_freq[c] == count[c]:
                    match += 1
            while match == expect:
                cur_len = r - l +1
                if cur_len < min_len:
                    min_len = cur_len
                    min_pos = [l,r]

                if s[l] in cur_freq:
                    if cur_freq[s[l]] == count[s[l]]:
                        match -= 1
                    cur_freq[s[l]]-=1
                l+=1
        print(min_pos)
        return '' if min_len == float('infinity') else s[min_pos[0]: min_pos[1] + 1]


