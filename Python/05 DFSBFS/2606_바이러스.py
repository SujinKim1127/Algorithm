n = int(input())
m = int(input())

visited = [0] * (n+1)
graph = [[False] * (n + 1) for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x][y] = True
    graph[y][x] = True

def DFS(v):
    visited[v] = 1
    for i in range(1, n+1):
        if visited[i] == 0 and graph[v][i]:
            print("v,i", v,i)
            DFS(i)

DFS(1)
print(sum(visited) - 1)