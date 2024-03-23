import sys
input = sys.stdin.readline

r, c = map(int, input().split())
graph = []
for _ in range(r):
    graph.append(list(input()))
visited = set()
answer = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def DFS(x, y, cnt):
    global answer
    answer = max(cnt, answer)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < r and 0 <= ny < c and not graph[nx][ny] in visited:
            visited.add(graph[nx][ny])
            DFS(nx, ny, cnt + 1)
            visited.remove(graph[nx][ny])
visited.add(graph[0][0])
DFS(0,0, 1)

print(answer)