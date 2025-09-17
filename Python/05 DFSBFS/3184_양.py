from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(input().strip()))

visited = [[0] * m for _ in range(n)]

def DFS(x, y):
    if x < 0 or x >= n or y < 0 or y >= m or visited[x][y] or graph[x][y] == "#": return (0,0)
    
    visited[x][y] = 1
    v = 1 if graph[x][y] == "v" else 0
    o = 1 if graph[x][y] == "o" else 0

    for dx, dy in [(1,0), (0,1), (-1, 0), (0, -1)]:
        nv, no = DFS(x + dx, y + dy)
        v += nv
        o += no
    
    return (v, o)
    
wolves = 0
sheeps = 0

for i in range(0, n):
    for j in range(0, m):
        if visited[i][j] == 0:
            # 한 영역 안에 있는 늑대와 양의 수
            wolf, sheep = DFS(i,j)
            if wolf >= sheep: wolves += wolf
            else: sheeps += sheep
                

print(sheeps, wolves)