import sys
sys.setrecursionlimit(100000)
r = sys.stdin.readline

n = int(r())

graph = []
for _ in range(n):
    graph.append(list(map(int, r().split())))

small = min(map(min,graph))
big = max(map(max,graph))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y, h):
    # 현재 위치 상하좌우로 재귀
    for m in range(4):
        nx = x + dx[m]
        ny = y + dy[m]
        
        # 주어진 범위를 넘어가면 종료     방문안한경우         높이보다 높은 영역만
        if 0 <= nx < n and 0 <= ny < n and not visit[nx][ny] and graph[nx][ny] > h:
            visit[nx][ny] = True    # 노드 방문 처리
            dfs(nx, ny, h)

result = 1

for h in range(big):
    visit = [[False] * n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] > h and not visit[i][j]:
                count += 1
                visit[i][j] = True
                dfs(i, j, h)        # 현재 위치에서 DFS 수행
    
    result = max(result, count)
    
print(result)

