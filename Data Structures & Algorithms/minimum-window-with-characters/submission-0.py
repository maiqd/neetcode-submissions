class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ''
        freq = {}

        for c in t:
            freq[c] = freq.get(c, 0) + 1
        freq2 = {}
        
        minLen = float("infinity")
        minPositions = [-1, -1]
        formed = 0
        expect = len(freq)
        l = 0
        for index, r in enumerate(s):
            if r in freq:
                freq2[r] = freq2.get(r,0) + 1
                if freq2[r] == freq[r]:
                    formed+=1
            
            while formed == expect:
                currLen = index - l + 1
                if currLen < minLen:
                    minLen = currLen
                    minPositions = [l, index]
                
                char_at_l = s[l]
                if char_at_l in freq:
                    if freq2[char_at_l] == freq[char_at_l]:
                        formed -= 1
                    freq2[char_at_l] -= 1
                l += 1
        return '' if minLen == float('infinity') else s[minPositions[0]: minPositions[1] + 1]