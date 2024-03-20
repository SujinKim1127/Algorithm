import sys
sys.setrecursionlimit(10**6)
m, n, k = map(int,input().split())

graph = [ [0] * (n) for _ in range(m)]
for _ in range(k):
    a, b, c, d = map(int, input().split())
    for y in range(a, c):
        for x in range(b, d):
            graph[x][y] = 1
cnt = 0
result = [0] *(m * n)
def DFS(x, y):
    global cnt
    if x >= m or x <= -1 or y >=n or y <= -1: return False
    else:
        if(graph[x][y] == 1): return False
        graph[x][y] = 1     # 방문 처리
        result[cnt] += 1
        DFS(x-1, y)
        DFS(x+1, y)
        DFS(x, y + 1)
        DFS(x, y - 1)
        
        

for x in range(0, m):
    for y in range(0, n):
        if graph[x][y] == 0:  
            DFS(x, y)
            cnt += 1

del result[cnt:]
result.sort()
print(cnt)
for i in range(cnt):
    print(result[i], end=' ')