class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ''
        freq = {}
        for i in t:
            freq[i] = freq.get(i,0) + 1
        
        current_freq = {}
        expect = len(freq)
        match = 0
        l = 0
        min_length = float("infinity")
        min_position = [0,0]
        for r, c in enumerate(s):
            if c in freq:
                current_freq[c] = current_freq.get(c, 0) + 1
                if current_freq[c] == freq[c]:
                    match+=1
            
            while match == expect:
                length = r - l + 1
                if length < min_length:
                    min_length = length
                    min_position = [l,r]
                if s[l] in current_freq:
                    if current_freq[s[l]] == freq[s[l]]:
                        match -=1
                    current_freq[s[l]] -= 1
                l+=1

        return '' if min_length == float('infinity') else s[min_position[0]:min_position[1]+1]