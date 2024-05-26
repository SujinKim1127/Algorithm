from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

queue = deque([1])
jump = [0] * (n+1)
visited = False
if n == 1: print(0)
else:
    while queue:
        x = queue.popleft()
        if x + arr[x-1] >= n:
            print(jump[x] + 1)
            visited = True
            break
        for i in range(1, arr[x-1]+1):
            if jump[x+i] == 0:
                queue.append(x + i)
                jump[x+i] = jump[x] + 1
    else: print(-1)


