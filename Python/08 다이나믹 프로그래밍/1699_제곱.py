import math

n = int(input())

dp = [x for x in range(n+1)]

for i in range(1, n + 1):
    for j in range(1, int(math.sqrt(i) + 1)):
        if dp[i] > (dp[i - j*j] + 1):
            dp[i] = dp[i- j*j] + 1

print(dp[n])