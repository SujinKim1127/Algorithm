import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [input().split() for _ in range(n)]

dp = [[0] * m for _ in range(n)]

dp[0][0] = int(graph[0][0])

for i in range(n):
    for j in range(m):
        cur = int(graph[i][j])

        if i + 1 < n:
            dp[i+1][j] = max(int(graph[i+1][j]) + dp[i][j], dp[i+1][j])
        if j + 1 < m:
            dp[i][j+1] = max(int(graph[i][j+1]) + dp[i][j], dp[i][j+1])


print(dp[-1][-1])
