class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)

        for s in strs:
            freq = [0] * 26
            for c in s:
                freq[ord(c) - ord('a')]+=1
            key = tuple(freq)

            res[key].append(s)
        print(res.values())
        return list(res.values())