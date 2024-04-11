import sys 
sys.setrecursionlimit(10000) 

t = int(input())

dx = [1, -1, 0 , 0]
dy = [0, 0, 1, -1]

def DFS(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if(0 <= nx < n) and (0 <= ny < m):
            if graph[nx][ny] == 1:
                graph[nx][ny] = -1
                DFS(nx, ny)

for _ in range(t):
    m,n,k = map(int, input().split())
    graph = [[0] * (m) for _ in range(n)]
    cnt = 0
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1
    for i in range(n):
        for j in range(m):
            if(graph[i][j] > 0 ):
                DFS(i, j)
                cnt += 1

    print(cnt)

from collections import deque


def BFS(x, y):
    queue = deque()
    queue.append([x, y])
    graph[x][y] = -1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if(0 <= nx < m) and (0 <= ny < n) and graph[nx][ny] == 1:
                    graph[nx][ny] = -1
                    queue.append([nx, ny])
    
for _ in range(t):
    m,n,k = map(int, input().split())
    graph = [[0] * (n) for _ in range(m)]
    cnt = 0
    for _ in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1
    for i in range(m):
        for j in range(n):
            if(graph[i][j] > 0 ):
                BFS(i, j)
                cnt += 1
    print(cnt)
