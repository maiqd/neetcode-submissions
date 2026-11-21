class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        seen = defaultdict(int)
        longest = 0
        for r in range(len(s)):
            while l < r and s[r] in seen and seen[s[r]] > 0:
                seen[s[l]] -= 1
                l += 1
            seen[s[r]] += 1
            longest = max(longest, r - l + 1)
        return longest
