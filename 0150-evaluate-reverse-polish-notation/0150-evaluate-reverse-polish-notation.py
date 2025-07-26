class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        ops = {"+", "-", "*", "/"}

        for token in tokens:
            if token not in ops:
                stack.append(int(token))
            else:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
            if token == "+":
                stack.append(num1+num2)
            elif token == "-":
                stack.append(num1-num2)
            elif token == "*":
                stack.append(num1*num2)
            elif token == "/":
                stack.append(int(num1/num2))

        return stack[-1]