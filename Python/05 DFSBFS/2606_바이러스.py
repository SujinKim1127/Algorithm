from collections import deque

n = int(input())
m = int(input())

visited = [False] * (n + 1)
graph = [[False] * (n + 1) for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x][y] = True
    graph[y][x] = True

def bfs(v):
    visited[v] = True
    queue = deque([v])
    result = 0

    while queue:
        v = queue.popleft()

        for i in range(1, n + 1):
            if visited[i] == False and graph[v][i]:
                queue.append(i)
                visited[i] = True
                result += 1
    
    return result

count = [0] * (n + 1)
def dfs(v):
    count[v] = 1
    for i in range(1, n+1):
        if count[i] == 0 and graph[v][i]:
            dfs(i)
    
    return sum(count)

            
print(bfs(1), dfs(1) - 1)