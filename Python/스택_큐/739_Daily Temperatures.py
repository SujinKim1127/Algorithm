class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []
        for i, t in enumerate(temperatures):
            # print(i, t)
            while stack and temperatures[stack[-1]] < t:
                # print(i, stack, temperatures[stack[-1]], stack[-1])
                prev_i = stack.pop()
                # print("prev", prev_i, i)
                answer[prev_i] = i - prev_i
                # print(answer)
            
            stack.append(i)
        # print(stack)
        return answer