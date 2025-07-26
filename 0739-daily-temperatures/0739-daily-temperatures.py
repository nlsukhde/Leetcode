class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []

        days = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                coolerIndex= stack.pop()
                days[coolerIndex] = i - coolerIndex
            stack.append(i)
        
        return days

        