from collections import deque
import sys
input = sys.stdin.readline

f, s, g, u, d = map(int, input().split())
count = [0] * (f + 1)

def BFS(start):
    queue = deque()
    queue.append(start)
    count[start] = 1
    while queue:
        v = queue.popleft()
        if v == g: 
            print(count[v]-1)
            return True
        for x in (v + u, v - d):
            if (0 < x <= f) and count[x] == 0:
                count[x] = count[v] + 1
                queue.append(x)
    return False

if not BFS(s): print("use the stairs")