import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n + 1)
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

cnt = 0

def DFS(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            DFS(graph, i, visited)

for i in range(1, n+1):
    if not visited[i]:
        DFS(graph, i, visited)
        cnt += 1

print(cnt)