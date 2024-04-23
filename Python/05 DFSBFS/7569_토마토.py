from collections import deque
import sys
input = sys.stdin.readline

m, n , h = map(int, input().split())

graph = []
queue = deque()

for i in range(h):
    arr = []
    for x in range(n):
        arr.append(list(map(int, input().split())))
        for y in range(m):
            if arr[x][y] == 1: queue.append([i, x, y])
    graph.append(arr)

dx = [ -1, 1, 0 , 0, 0, 0]
dy = [ 0, 0, 1, -1, 0, 0]
dz = [ 0 , 0, 0, 0, -1, 1]

def BFS():
    while queue:
        x, y, z = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if (0 <= nx < h) and (0 <= ny < n) and (0 <= nz < m) and graph[nx][ny][nz]==0:
                graph[nx][ny][nz] = graph[x][y][z] + 1
                queue.append([nx, ny, nz])

BFS()

answer = 0
for k in range(h):
    for i in range(n):
        for j in range(m):
            if graph[k][i][j] == 0:
                print(-1)
                exit(0)
        answer = max(max(graph[k][i]), answer)

print(answer - 1)