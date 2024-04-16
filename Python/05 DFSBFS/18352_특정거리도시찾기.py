import sys
input=sys.stdin.readline
from collections import deque

n,m,k,X = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [0] * (n+1)
visited = [False] * (n+1)
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
result = []
def BFS(x):
    queue = deque()
    queue.append(x)
    visited[x] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                distance[i] += distance[v] + 1
                if distance[i] == k:
                    result.append(i)

BFS(X)
if len(result) == 0: print(-1)
else: 
    result.sort()
    for i in result:
        print(i)