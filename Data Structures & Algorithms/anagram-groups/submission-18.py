class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        for s in strs:
            # key =  ''.join(sorted(s))
            arr = [0] * 26
            for c in s:
                arr[ord(c) - ord('a')]  = arr[ord(c) - ord('a')] + 1
            key = tuple(arr)
            group[key].append(s)
        
        return list(group.values())