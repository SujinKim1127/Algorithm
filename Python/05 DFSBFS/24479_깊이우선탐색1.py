import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

n, m, r = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

cnt = 1

def DFS(graph, v, visited):
    global cnt
    visited[v] = cnt
    graph[v].sort()
    for i in graph[v]:
        if visited[i] == 0:
            cnt += 1
            DFS(graph, i, visited)

DFS(graph, r, visited)

for i in range(1, n + 1):
    print(visited[i])
