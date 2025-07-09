class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+','-','*','/'}

        for i in range(len(tokens)):
            if tokens[i] in operators:
                num2 = stack.pop()
                num1 = stack.pop()
                if tokens[i] == '/':
                    output = int(num1/num2)
                    stack.append(output)
                else:
                    strExp = str(num1) + tokens[i] + str(num2)
                    output = eval(strExp)
                    stack.append(output)
            else:
                stack.append(int(tokens[i]))

        return stack[-1]