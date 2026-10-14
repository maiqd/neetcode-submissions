class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracketDict = {"[": "]", "{": "}", "(": ")"}
        for c in s:
            if c in bracketDict:
                stack.append(c)
            else:
                if not stack:
                    return False
                openBracket = stack.pop()
                if bracketDict[openBracket] != c:
                    return False
        return not stack
