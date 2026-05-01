class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list[str])
        for s in strs:
            # key = ''.join(sorted(s))
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            key = tuple(count)
            res[key].append(s)
        return list(res.values())