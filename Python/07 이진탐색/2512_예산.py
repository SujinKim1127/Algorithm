n = int(input())
req = list(map(int, input().split()))
budget = int(input())
start, end = 0, max(req)

while start <= end:
    mid = (start + end) // 2    # 우선 중간값으로 시작
    total = 0
    for x in req:
        if x >= mid:        # 상한액보다 크면
            total += mid    # 상한액 더하기
        else:               # 상한액보다 작으면
            total += x      # 요청 금액 더하기

    if total <= budget:     # 구한 총액이 예산보다 작으면
        start = mid + 1      
    else:                   # 구한 총액이 예산보다 크면
        end = mid -1

print(end)
