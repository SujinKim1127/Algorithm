import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * (n+1)
t = []
p = []
for i in range(1, n+1):
    a,b = map(int, input().split())
    t.append(a)
    p.append(b)

for i in range(n-1, -1, -1):
    if (i + t[i] > n):
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], dp[t[i] + i] + p[i])

print(dp[0])