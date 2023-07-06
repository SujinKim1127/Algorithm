n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

number = []

for i in range(n):
    number.append(arr[i])

number.sort(reverse=True)

result = 0
cnt = 0

for i in range(m):
    if(cnt == k):
        result += number[1]
        cnt = 0
    else:
        result += number[0]
        cnt += 1

print(result)


## 답안 예시
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

count = int(m / (k+1)) * k
count += m % (k+1)

result = 0
result += count * first
result += (m - count) * second