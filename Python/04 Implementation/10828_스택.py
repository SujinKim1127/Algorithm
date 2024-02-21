import sys
input = sys.stdin.readline

n = int(input())
stack = []
for _ in range(n):
    str = input()
    arr = str.split()
    if arr[0] == 'push':
        stack.append(arr[1])
    elif arr[0] == 'pop': 
        if len(stack) > 0: print(stack.pop())
        else: print(-1)
    elif arr[0] == 'size': print(len(stack))
    elif arr[0] == 'empty':
        if len(stack) > 0 : print(0)
        else: print(1)
    elif arr[0] == 'top':
        if len(stack) > 0: print(stack[-1])
        else: print(-1)