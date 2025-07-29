class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            print(stack)
            if op == "+":
                stack.append(int(stack[-1]) + int(stack[len(stack)-2]))
            elif op == "D":
                doubled = int(stack[-1]) * 2
                stack.append(doubled)
            elif op == "C":
                stack.pop()
            else:
                stack.append(int(op))
        
        return sum(stack)
            
        