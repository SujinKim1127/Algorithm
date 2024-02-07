n = int(input())
arr = list(map(int, input().split()))
arr.sort()
answer = 0
for i in range(n):
    temp = arr[:i] + arr[i+1:] # 현재 비교 원소 제외하고
    start = 0
    end = len(temp) - 1
    while start < end:
        sum = temp[start] + temp[end]
        if sum > arr[i]:
            end -= 1
        elif sum < arr[i]:
            start += 1
        else:
            answer += 1
            break

print(answer)
