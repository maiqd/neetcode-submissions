class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        count_t = Counter(t)
        count_s = defaultdict(int)
        matches = 0
        l = 0
        min_length = float("inf")
        pos = [0, 0]
        target = len(count_t)
        for r, c in enumerate(s):
            if c in count_t:
                count_s[c] += 1
                if count_s[c] == count_t[c]:
                    matches += 1
                while matches == target:
                    key = s[l]
                    if key in count_t and count_s[key] == count_t[key]:
                        matches -= 1
                    count_s[key] -= 1
                    if r - l + 1 < min_length:
                        min_length = r - l + 1
                        pos = [l, r]
                    l += 1
        return "" if min_length == float("inf") else s[pos[0] : pos[1] + 1]
