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
        stack = []
        pairs = {
            "}":"{",
            ")":"(",
            "]":"["
        }

        for c in s:
            if c in pairs:
                if not stack or stack.pop() != pairs[c]: return False
            else: stack.append(c)
        
        print(stack)
        return not stack