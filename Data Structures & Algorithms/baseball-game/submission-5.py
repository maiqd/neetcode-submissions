class Solution:
    def calPoints(self, operations: List[str]) -> int:

        stack = []
        s = 0
        for operation in operations:
            if operation == "+":
                add = stack[-1] + stack[-2]
                stack.append(add)
                s += add
            elif operation == "D":
                double = stack[-1] * 2
                stack.append(double)
                s += double
            elif operation == "C":
                val = stack.pop()
                s -= val
            else:
                num = int(operation)
                stack.append(num)
                s += num

        return s
