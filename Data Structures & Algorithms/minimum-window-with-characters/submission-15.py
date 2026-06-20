class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        count_t = Counter(t)
        window = defaultdict(int)

        matches = 0
        need = len(count_t)
        min_len = float("inf")
        min_pos = [-1, -1]

        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] += 1

            if c in count_t and window[c] == count_t[c]:
                matches += 1

            while matches == need:
                key = s[l]
                if key in count_t:
                    if r - l + 1 < min_len:
                        min_len = r - l + 1
                        min_pos = [l, r]
                    if window[key] == count_t[key]:
                        matches -= 1
                window[key] -= 1
                l += 1
        return "" if min_len == float("inf") else s[min_pos[0] : min_pos[1] + 1]
