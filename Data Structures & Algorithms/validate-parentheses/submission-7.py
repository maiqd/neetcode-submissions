class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openParenthesesMap = {"[": "]", "{": "}", "(": ")"}

        for c in s:
            if c in openParenthesesMap:
                stack.append(c)
            else:
                if not stack:
                    return False
                openBracket = stack.pop()
                if openParenthesesMap[openBracket] != c:
                    return False

        return not stack
