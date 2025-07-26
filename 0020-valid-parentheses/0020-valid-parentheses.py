class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char == '(':
                stack.append('(')
            elif char == '{':
                stack.append('{')
            elif char == '[':
                stack.append('[')
            elif char == ')' and stack and stack[-1] == '(':
                stack.pop()
            elif char == '}' and stack and stack[-1] == '{':
                stack.pop()
            elif char == ']' and stack and stack[-1] == '[':
                stack.pop()
            else:
                return False
            
            print(stack)  # Optional debug statement

        return len(stack) == 0


        