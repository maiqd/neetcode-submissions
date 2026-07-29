from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        count_t = Counter(t)
        count_s = defaultdict(int)
        
        matches = 0
        target = len(count_t)
        
        min_len = float("inf")
        min_pos = (0, 0)
        
        l = 0
        for r in range(len(s)):
            char = s[r]
            
            # Only track characters present in t
            if char in count_t:
                count_s[char] += 1
                if count_s[char] == count_t[char]:
                    matches += 1

            # Contract window from the left
            while matches == target:
                if (r - l + 1) < min_len:
                    min_len = r - l + 1
                    min_pos = (l, r)

                left_char = s[l]
                if left_char in count_t:
                    if count_s[left_char] == count_t[left_char]:
                        matches -= 1
                    count_s[left_char] -= 1
                
                l += 1

        return "" if min_len == float("inf") else s[min_pos[0] : min_pos[1] + 1]