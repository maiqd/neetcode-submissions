class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += f"{len(s)}#{s}"
        return res

    def decode(self, s: str) -> List[str]:
        r = 0
        res = []
        while r < len(s):
            l = r
            while r < len(s) and s[r] != "#":
                r += 1
            num = int(s[l:r])
            l = r + 1
            r = l + num
            res.append(s[l:r])
        return res
