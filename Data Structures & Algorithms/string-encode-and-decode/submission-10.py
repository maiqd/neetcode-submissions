class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += f"{len(s)}#{s}"
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i + 1
            while j < len(s) and s[j] != "#":
                j += 1
            count = int(s[i:j])

            i = j + 1
            j = i + count

            res.append(s[i:j])
            i = j
        return res
