import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x:(x[1], x[0]))
last = 0
count = 0
for x in arr:
    if x[0] >= last:
        last = x[1]
        count += 1

print(count)