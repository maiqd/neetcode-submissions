class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c in ('[', '{', '('):
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                openChar = stack.pop()
                if (c == ']' and openChar != '[') or (c == ')' and openChar != '(') or (c == '}' and openChar != '{'):
                    return False
        return len(stack) == 0