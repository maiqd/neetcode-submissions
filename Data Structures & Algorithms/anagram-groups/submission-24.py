class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        group = defaultdict(list)
        for s in strs:
            keyArr = [0] * 26
            for c in s:
                keyArr[ord(c) - ord("a")] += 1
            key = tuple(keyArr)
            group[key].append(s)

        return list(group.values())
