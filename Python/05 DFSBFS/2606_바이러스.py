n = int(input())
m = int(input())

visited = [0] * (n+1)
graph = [[False] * (n + 1) for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x][y] = True
    graph[y][x] = True

def DFS(v):
    visited[v] = 1
    for i in range(1, n+1):
        if visited[i] == 0 and graph[v][i]:
            print("v,i", v,i)
            DFS(i)

DFS(1)
print(sum(visited) - 1)

from collections import deque

n = int(input())
net = int(input())

visited = [False] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(net):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def BFS(x):
    q = deque()
    q.append(x)
    visited[x]=True
    result = 0
    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                result += 1
    return result

print(BFS(1))