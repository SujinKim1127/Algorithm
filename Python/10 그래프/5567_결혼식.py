from collections import deque
import sys
input=sys.stdin.readline

n = int(input())
m = int(input())

visited = [False for _ in range(n+1)]
friend = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    friend[x].append(y)
    friend[y].append(x)

def BFS(node):
    queue = deque()
    queue.append([node,0])
    visited[node] = True
    count = 0
    while queue:
        [x, cnt] = queue.popleft()
        print(x, cnt)
        for i in friend[x]:
            if not visited[i] and cnt < 2:
                visited[i] = True
                queue.append([i, cnt + 1])
                count += 1
    
    return count

print(BFS(1))
