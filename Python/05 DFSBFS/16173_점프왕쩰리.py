n = int(input())
graph = []
visit = [[0]*n for _ in range(n)]
for _ in range(n):
    graph.append(list(map(int, input().split())))   

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= n or visit[x][y] == 1:
        return 
    if graph[x][y] == -1: 
        visit[x][y] = 1
        return
    
    visit[x][y] = 1

    dfs(x, y + graph[x][y])
    dfs(x+graph[x][y], y)
    
dfs(0,0)
if visit[-1][-1] == 1: print("HaruHaru")
else: print("Hing")


from collections import deque
n = int(input())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))   

visit = [[False]*n for _ in range(n)]

dx = [1, 0]
dy = [0, 1]

def bfs(x, y):
    q = deque()
    q.append([x,y])

    while q:
        x, y = q.popleft()
        step = graph[x][y]  # 현재 위치 값

        if graph[x][y] == -1:
            return True
        for move in range(2):
            nx = x + dx[move] * step
            ny = y + dy[move] * step

            # 범위 벗어남
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if not visit[nx][ny]:
                visit[nx][ny] = True
                q.append([nx,ny])

if bfs(0, 0):
    print('HaruHaru')
else: print('Hing')



