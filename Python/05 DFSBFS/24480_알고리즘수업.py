import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

n, m, r = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m) :
    x, y = map(int ,input().split())
    graph[x].append(y)
    graph[y].append(x)

cnt = 1

def DFS(v):
    global cnt
    graph[v].sort(reverse=True)     # 내림차순 정렬
    visited[v] = cnt      # 방문처리
    for i in graph[v]:
        if(visited[i] == 0): # 방문 안했으면    
            cnt += 1
            DFS(i)
    


DFS(r)

for i in range(1, n+1):
    print(visited[i])