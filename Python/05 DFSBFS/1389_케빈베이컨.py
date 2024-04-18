from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] * (n+1) for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def BFS(start, end):
    queue = deque()
    queue.append(start)
    visited = [0] * (n+1)
    while queue:
        v = queue.popleft()
        if v == end: return visited[v]
        for x in graph[v]:
            if visited[x] == 0:
                visited[x] = visited[v] + 1
                queue.append(x)

arr = []
for x in range(1, n+1):
    result = 0
    for y in range(1, n + 1):
        bfs = BFS(x,y)
        result += bfs
    arr.append(result)

small = min(arr)
print(arr.index(small)+1)