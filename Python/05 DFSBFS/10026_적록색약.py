import sys
sys.setrecursionlimit(10**6) # 파이썬의 재귀 깊이 지정 (Python3)
input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(input()))

visited = [[0] * n for _ in range(n)]
no_cnt = 0
yes_cnt = 0

def DFS(x, y, v):
    if x >= n or x <= -1 or y >= n or x <= -1 or visited[x][y] == 1: return False
    else:
        if(v == graph[x][y]):
            visited[x][y] = 1 # visited
            DFS(x+1, y, v)
            DFS(x-1, y, v)
            DFS(x, y+1, v)
            DFS(x, y-1, v)

for i in range(0, n):
    for j in range(0, n):
        if visited[i][j] == 0:
            DFS(i,j, graph[i][j])
            no_cnt += 1

for x in range(0, n):
    for y in range(0, n):
        if(graph[x][y] == 'G'): graph[x][y] = 'R'

visited = [[0] * n for _ in range(n)]

for i in range(0, n):
    for j in range(0, n):
        if visited[i][j] == 0:
            DFS(i, j, graph[i][j])
            yes_cnt += 1

print(no_cnt, yes_cnt)




##-------------------------------------------------------------------------
import copy
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(input()))

X_graph = copy.deepcopy(arr)
O_graph = copy.deepcopy(arr)

for x in range(0, n):
    for y in range(0, n):
        if(O_graph[x][y] == 'G'): O_graph[x][y] = 'R'

no_cnt = 0
yes_cnt = 0
def DFS(x, y, graph, v):
    if x >= n or x <= -1 or y >= n or x <= -1 or graph[x][y] == 0: return False
    else:
        if(v == graph[x][y]):
            graph[x][y] = 0 # visited
            DFS(x+1, y, graph, v)
            DFS(x-1, y, graph, v)
            DFS(x, y+1, graph, v)
            DFS(x, y-1, graph, v)

for i in range(0, n):
    for j in range(0, n):
        if X_graph[i][j] != 0:
            DFS(i,j,X_graph, X_graph[i][j])
            no_cnt += 1

        if O_graph[i][j] != 0:
            DFS(i, j, O_graph, O_graph[i][j])
            yes_cnt += 1

print(no_cnt, yes_cnt)