class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        s = 0
        for operation in operations:
            print(operation, stack)
            if operation == "+":
                score = stack.pop()
                sum_score = stack[-1] + score
                stack.append(score)
                stack.append(sum_score)
                s += sum_score
            elif operation == "D":
                new_score = stack[-1] * 2
                stack.append(new_score)
                s += new_score
            elif operation == "C":
                score = stack.pop()
                s -= score
            else:
                num = int(operation)
                stack.append(num)
                s += num
        return s
