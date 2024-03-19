import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

dx = [1, -1, 0 , 0]
dy = [0, 0 , 1, -1]

n, m = map(int, input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(str, input())))

def DFS(x, y):
    global cnt
    if x <= -1 or y >= m or x >= n or y <= -1: return False
    else:
        if graph[x][y] == 'P':
            cnt += 1
        if graph[x][y] == 'O':
            graph[x][y] = '1' # 방문 처리
            DFS(x - 1, y)
            DFS(x + 1, y)
            DFS(x, y + 1)
            DFS(x, y - 1)
        
cnt = 0
start = [[i,j] for i in range(n) for j in range(m) if graph[i][j]=="I"]
DFS(start[0][0], start[0][1])

if(cnt == 0): print("TT")
else: print(cnt)