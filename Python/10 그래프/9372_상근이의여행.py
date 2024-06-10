import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    cnt = 0
    graph = [[] for _ in range(n + 1)]
    visited = [False for _ in range(n+1)]

    def solve(node, cnt):
        visited[node] = True
        for x in graph[node]:
            if visited[x] == False:
                cnt = solve(x, cnt + 1)
        return cnt

    for _ in range(m):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    cnt = solve(1, 0)
    print(cnt)



