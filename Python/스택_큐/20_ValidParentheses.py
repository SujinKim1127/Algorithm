class Solution:
    def isValid(self, s: str) -> bool:

        arr = deque(list(s))
        if len(arr) % 2 == 1: return False

        stack = []

        left = ["(", "{", "["]
        right = [")", "}", "]"]

        while arr:
            char = arr.popleft()
            if char in left:
                stack.append(char)
            else:
                if len(stack) == 0: return False
                top = stack.pop()
                idx = left.index(top)
                if char != right[idx]: return False
        
        if len(stack) != 0: return False
        return True

    # 더 빠른 풀이
    def isValid(self, s: str) -> bool:
        pairs = {
            "}": "{",
            ")":"(",
            "]":"[",
        }

        stack = []
        for char in s:
            # 닫힌 괄호일때
            if char in pairs:
                # 빈값에 닫힌 괄호 들어가거나 닫힌괄호의 짝이 없을때
                if not stack or stack.pop() != pairs[char]:
                    return False
            # 열린 괄호이면 append
            else:
                stack.append(char)
        
        # stack에는 빈값만 있어야함
        return not stack