n, m, visit = map(int, input().split())

visited = [False] * (n + 1)
graph = [[False] * (n + 1) for _ in range(n+1)]

for i in range(m):
    x, y = map(int, input().split())
    graph[x][y] = True
    graph[y][x] = True

def dfs(v):
    visited[v] = True
    print(v, end=' ')
    for i in range(1, n + 1):
        if visited[i] == False and graph[v][i]:
            dfs(i)


b_visited = [False] * (n + 1)

from collections import deque

def bfs(start):
    queue = deque([start])
    b_visited[start] = True
    
    while queue:
        start = queue.popleft()
        print(start, end=" ")

        for i in range(1, n + 1):
            if b_visited[i] == False and graph[start][i]:
                queue.append(i)
                b_visited[i] = True




dfs(visit)
print()
bfs(visit)