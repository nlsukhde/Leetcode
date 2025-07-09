class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    #       my_stack = []
    # my_stack.append(10) # Push 10
    # my_stack.append(20) # Push 20
    # popped_element = my_stack.pop() # Pop 20
    #  top_element = my_stack[-1] # Peek 10

        retval= [0] * len(temperatures)

        stack = []

        for i in range(len(temperatures)):
            while len(stack) > 0 and temperatures[i] > stack[-1][0]:
                retval[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            stack.append((temperatures[i],i))

        return retval
        