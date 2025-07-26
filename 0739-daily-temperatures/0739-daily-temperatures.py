class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []

        days = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                warmer = stack.pop()
                days[warmer[1]] = i - warmer[1]
            stack.append((temperatures[i],i))
        
        return days

        