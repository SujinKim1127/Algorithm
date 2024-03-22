n = int(input())

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
dp = [0] * 3001

# bottom up DP
for i in range(2, n + 1):
    # 현재의 수에서 1을 빼는 경우
    dp[i] = dp[i-1] + 1

    # 2로 나누어떨어지는 경우
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    
    # 3으로 나누어떨어지는 경우
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
    # 5로 나누어떨어지는 경우
    if i % 5 == 0:
        dp[i] = min(dp[i], dp[i // 5] + 1)
    print(i, dp[i])

print(dp[n])