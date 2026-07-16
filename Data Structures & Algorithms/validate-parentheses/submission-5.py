class Solution:
    def isValid(self, s: str) -> bool:
        compare = dict()
        compare["("] = ")"
        compare["{"] = "}"
        compare["["] = "]"
        stack = []
        for c in s:
            if c in compare:
                stack.append(c)
            else:
                if not stack:
                    return False
                open = stack.pop()
                if compare[open] != c:
                    return False

        return len(stack) == 0
