import sys
input = sys.stdin.readline

n, k  = map(int, input().split())

bag = []
for _ in range(n):
    bag.append(list(map(int, input().split())))

dp = [[0] * (k+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):     # 최대 무게까지
        if j >= bag[i-1][0]:    # 현재 최대 무게가 해당 물건무게보다 크면

            # 현재 물건 가치 + 이전 물건 가치의 최대값
            dp[i][j] = max(bag[i-1][1] + dp[i-1][j - bag[i-1][0]], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][k])
