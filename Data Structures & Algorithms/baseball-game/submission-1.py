class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        res = 0
        for o in operations:
            if o == "+":
                num = stack[-1] + stack[-2]
                stack.append(num)
                res += num
            elif o == "D":
                num = stack[-1] * 2
                stack.append(num)
                res += num
            elif o == "C":
                val = stack.pop()
                res -= val
            else:
                num = int(o)
                stack.append(num)
                res += num
        return res
