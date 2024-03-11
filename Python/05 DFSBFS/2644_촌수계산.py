n = int(input())
first, second = map(int, input().split())
m = int(input())
visited =  [False] * (n + 1)
graph = [[False] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x][y] = True
    graph[y][x] = True

cnt = 0
result = []
def DFS(v, cnt):
    cnt += 1
    visited[v]= True
    if v == second:
        result.append(cnt)
    else:
        for i in range(1, n + 1):
            if visited[i] == False and graph[v][i]:
                DFS(i, cnt)

DFS(first, 0)
if(len(result) == 0): print(-1)
else: print(result[0] - 1)