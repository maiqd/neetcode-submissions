class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {"{": "}", "[": "]", "(": ")"}
        for c in s:
            if c in dic:
                stack.append(c)
            else:
                if not stack:
                    return False
                openBrackets = stack[-1]
                if c == dic[openBrackets]:
                    stack.pop()
                else:
                    return False
        return False if stack else True
