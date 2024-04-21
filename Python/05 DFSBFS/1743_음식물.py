from collections import deque
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = [[0]* m for _ in range(n)]
for _ in range(k):
    x, y = map(int, input().split())
    graph[x-1][y-1]=1

dx= [-1, 1, 0 , 0]
dy = [0, 0, 1, -1]

def BFS(a, b):
    queue = deque()
    queue.append([a,b])
    cnt = 0
    while queue:
        [x, y] = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < n) and (0 <= ny < m):
                if graph[nx][ny] > 0:
                    cnt += 1
                    queue.append([nx, ny])
                    graph[nx][ny] = -1
                elif graph[nx][ny] == 0: graph[nx][ny] = -1
    if cnt == 0: cnt += 1
    return cnt


ans = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            ans = max(BFS(i,j), ans)

print(ans)                    
