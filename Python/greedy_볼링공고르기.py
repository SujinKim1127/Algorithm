n, m = map(int, input().split())
data = list(map(int, input().split(' ')))

weight = []

for i in range(n):
    weight.append(data[i])

result = 0


## 시간이 n^2 라서 시간복잡도가 별로임
for i in range(n):
    for j in range(i):
        if(weight[i] != weight[j]): result += 1

print(result)


###################################
arr = [0] * 11
for x in weight:
    arr[x] += 1

cnt = 0

for i in range(1, m + 1):
    n -= arr[i]
    cnt += arr[i] * n

print(cnt)