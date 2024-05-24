import sys
input = sys.stdin.readline


n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

left = min(arr)
right = sum(arr)

while left <= right:
    mid = (left + right) // 2
    charge = mid
    num = 1     # 횟수
    for i in range(n):
        if charge < arr[i]: # 돈이 부족하면
            charge = mid
            num += 1
        charge -= arr[i] # 돈이 충분하거나 딱 알맞아서 그날 돈 다 쓰기
    
    if num > m or mid < max(arr):   # m보다 많이 인출하거나 인출금액이 적을 경우
        left = mid + 1
    else: # 인출 금액이 많은 경우
        right = mid - 1
        k = mid # k 값 저장

print(k)