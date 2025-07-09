class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        retval= [0] * len(temperatures)

        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()
                retval[index] = i - index
            stack.append(i)

        return retval
        