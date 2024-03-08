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
