class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores_stack = []
        for op in operations:
            if op == "C":
                scores_stack.pop()
            elif op == "+":
                scores_stack.append(scores_stack[-1] + scores_stack[-2])
            elif op == "D":
                scores_stack.append(scores_stack[-1] * 2)
            else:
                scores_stack.append(int(op))
        return sum(scores_stack)
