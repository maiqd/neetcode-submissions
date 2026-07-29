class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        count_t = Counter(t)
        count_s = defaultdict(int)
        matches = 0
        target = len(count_t)

        minLength = float("inf")
        minPos = [0, 0]
        l = 0
        for r in range(len(s)):
            key = s[r]
            count_s[key] += 1

            if key in count_t:
                if count_s[key] == count_t[key]:
                    matches += 1
                while matches == target:
                    print(s[l : r + 1])
                    if r - l + 1 < minLength:
                        minLength = r - l + 1
                        minPos = [l, r]

                    if count_s[s[l]] == count_t[s[l]]:
                        matches -= 1
                    count_s[s[l]] -= 1
                    l += 1

        return "" if minLength == float("inf") else s[minPos[0] : minPos[1] + 1]
