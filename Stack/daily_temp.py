class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        answer = [0] * len(temperatures)
        stack = []

        for t in range(len(temperatures)):
            current_temp = temperatures[t]
            
            while stack and temperatures[stack[-1]] < current_temp:
                index = stack.pop()
                answer[index] = abs(t - index)
            
            stack.append(t)
                               
        return answer
