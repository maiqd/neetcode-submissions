class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        sum = 0
        for operation in operations:
            if operation == "+":
                val1 = stack.pop()
                val2 = stack[-1]
                res = val1 + val2
                stack.append(val1)
                stack.append(res)
                sum += res
            elif operation == "D":
                res = stack[-1] * 2
                stack.append(res)
                sum += res
            elif operation == "C":
                pre = stack.pop()
                sum -= pre
            else:
                val = int(operation)
                stack.append(val)
                sum += val
        return sum
