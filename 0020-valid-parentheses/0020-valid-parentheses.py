class Solution:
    def isValid(self, s: str) -> bool:
        
        bracketmap = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        stack = []

        for char in s:
            if char not in bracketmap:
                stack.append(char)
            #close bracket case
            elif char in bracketmap and len(stack) > 0:
                if stack[-1] == bracketmap[char]:
                    stack.pop()
                else:
                    return False
            else:
                return False
        
        if len(stack) == 0:
            return True
        else:
            return False

        