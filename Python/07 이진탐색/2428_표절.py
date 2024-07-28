import sys
input = sys.stdin.readline

n = int(input())
files = sorted(list(map(int, input().split())))
res = 0
for x in range(n):
    start, end = x, n
    # print(x + 10000000)
    while start < end:
        m = (start + end) // 2
        # print(files[x], files[m])
        if files[x] >= 0.9 * files[m]:
            start = m + 1
        else: end = m
    res += end - x - 1

print(res)

# 8
# 9 10 10 10 10 11 11 12

