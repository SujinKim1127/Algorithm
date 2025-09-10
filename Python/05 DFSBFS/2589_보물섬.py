from collections import deque
import sys
input = sys.stdin.readline

dx= [-1, 1, 0 , 0]
dy = [0, 0, 1, -1]

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(input().strip()))


def BFS(a,b):
    queue = deque([(a,b)])
    distance = [[-1] * m for _ in range(n)]
    distance[a][b] = 0 # 출발점 처리
    far = 0
    while queue:
      x, y = queue.popleft()
      far = max(far, distance[x][y])
      for i in range(4):
         nx = x + dx[i]
         ny = y + dy[i]
         
         if(0<=nx < n) and (0 <= ny < m) and graph[nx][ny] == "L" and distance[nx][ny] == -1:
            queue.append((nx, ny))
            distance[nx][ny] = distance[x][y] + 1
    return far

answer = 0
for i in range(n):
   for j in range(m):
      if graph[i][j] == "L":
         answer = max(answer, BFS(i,j))

print(answer)