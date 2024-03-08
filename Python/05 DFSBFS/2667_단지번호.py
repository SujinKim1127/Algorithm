n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

arr = [0] * (n*n)
cnt = 0
def DFS(x, y):
    global cnt
    if x <= -1 or y >= n or x >= n or y <= -1: return False
    else:
        if graph[x][y] == 1:
            arr[cnt] += 1
            graph[x][y] = 0  # 방문처리
            DFS(x - 1, y)
            DFS(x + 1, y)
            DFS(x, y + 1)
            DFS(x, y - 1)

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            DFS(i,j)
            cnt += 1
del arr[cnt:]
arr.sort()
print(cnt)
for i in range(cnt):
    print(arr[i])