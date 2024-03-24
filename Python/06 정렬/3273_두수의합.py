n = int(input())
arr = list(map(int, input().split()))
x = int(input())

arr.sort()

answer = 0
left = 0
right = n -1

while left < right:
    temp = arr[left] + arr[right]
    if temp == x:
        answer += 1
        left += 1
    elif temp < x:
        left += 1
    else: right -= 1

print(answer)