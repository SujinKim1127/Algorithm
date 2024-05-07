import sys
input = sys.stdin.readline

n = int(input())

# 2 = 10           # 1
# 3 = 100 101     # 2
# 4 = 1000 1001 1010      # 3
# 5 = 10000 10001 10100 10101 10010   # 5
# 6 = 100001 100010 101001 101000 101010 100101 100100 100000     #8

dp = [0] * (n+1)
dp[1] = 1

if n > 1: dp[2] = 1

if n > 2:
    for i in range(3, n+1):
        dp[i] = dp[i - 1] + dp[i - 2]

print(dp[n])