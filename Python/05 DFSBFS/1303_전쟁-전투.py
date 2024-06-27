from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(input()))

dx = [-1, 1, 0 , 0]
dy = [0, 0, -1, 1]



def BFS(a, b):
    queue = deque()
    queue.append([a, b])
    cur = graph[a][b]
    graph[a][b] = 1
    cnt = 0
    while queue:
        [x, y] = queue.popleft()
        cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < n) and (0 <= ny < m) and graph[nx][ny] == cur:
                
                queue.append([nx, ny])
                graph[nx][ny] = -1
    return cnt

w = 0
b = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == "W":
            w += (BFS(i, j))**2
        if graph[i][j] == "B":
            b += (BFS(i, j)) ** 2

print(w)
print(b)

            
            