import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

from collections import deque

n = int(input())
graph = [[] for _ in range(n+1) ]
visited = [0] * (n + 1)
for _ in range(n-1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def BFS(v):
    queue = deque()
    queue.append(v)
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if visited[i] == 0:
                visited[i] = x
                queue.append(i)

BFS(1)
for i in range(2, n + 1):
    print(visited[i])

def DFS(v):
    for i in graph[v]:
        if visited[i] == 0:
            visited[i] = v
            DFS(i)

DFS(1)
for i in range(2, n + 1):
    print(visited[i])