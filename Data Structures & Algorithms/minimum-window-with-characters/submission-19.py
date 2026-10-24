class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        count_s = defaultdict(int)
        count_t = Counter(t)

        shortest_len = float("inf")
        shortes_pos = (0, 0)

        l = 0
        matches = 0
        target = len(count_t)
        for r in range(len(s)):
            count_s[s[r]] += 1

            if count_s[s[r]] == count_t[s[r]]:
                matches += 1

            while matches == target:
                if r - l + 1 < shortest_len:
                    shortest_len = r - l + 1
                    shortes_pos = (l, r)

                count_s[s[l]] -= 1
                if count_s[s[l]] + 1 == count_t[s[l]]:
                    matches -= 1
                l += 1

        return "" if shortest_len == float("inf") else s[shortes_pos[0] : shortes_pos[1] + 1]
