from collections import deque
import sys
input = sys.stdin.readline

dx= [-1, 1, 0 , 0]
dy = [0, 0, 1, -1]

m, n = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

queue = deque()

def BFS():
    while queue:
        [x, y] = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0<=nx < n) and (0 <= ny < m) and graph[nx][ny]==0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append([nx,ny])

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append([i, j])

BFS()


arr = [(i, j) for i in range(n) for j in range(m) if graph[i][j]==0]
answer = max(max(i) for i in graph)
if len(arr) == 0: print(answer-1)
else: print(-1)

