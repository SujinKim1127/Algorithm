import sys
input = sys.stdin.readline

n = int(input())

graph = [input().split() for _ in range(n)]

dp = [[0] * n for _ in range(n)]

dp[0][0] = 1

for i in range(n):
    for j in range(n):
        cur = int(graph[i][j])
        if cur == 0 or dp[i][j] == 0:
            continue
        if i + cur < n:    # 아래로 이동
            dp[i+cur][j] += dp[i][j]
        if j + cur < n:    # 오른족으로 이동
            dp[i][j+cur] += dp[i][j]


print(dp[-1][-1])
