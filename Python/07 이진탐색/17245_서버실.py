import sys
input = sys.stdin.readline

n = int(input())

pcs = []
for _ in range(n):
    pcs.append(list(map(int, input().split())))

pc = sum(pcs, [])
pc.sort()
start, end = 0, pc[-1]
goal = sum(pc) / 2
ans = 0
while start <= end:
    mid = (start + end) // 2
    # print("mid", mid)
    count = 0
    for x in pc:
        if x >= mid: count += mid
        else: count += x
    if count >= goal:
        end = mid - 1
        ans = mid
    else: start = mid + 1

print(ans)