class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {"(": ")", "{": "}", "[": "]"}
        stack = []
        for c in s:
            if c in bracket_map:
                stack.append(c)
            else:
                if not stack:
                    return False
                top_bracket = stack.pop()
                if bracket_map[top_bracket] != c:
                    return False

        return not stack
