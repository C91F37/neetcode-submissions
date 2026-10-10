class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # monotonic, stores index waiting for warmer day.
        result = [0 for _ in range(len(temperatures))]
        for i, x in enumerate(temperatures):
            while stack and x > temperatures[stack[-1]]:
                ind = stack.pop()
                result[ind] = i - ind
            stack.append(i)
        return result