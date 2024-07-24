import sys
input = sys.stdin.readline

s, c = map(int, input().split())
pas = []
for _ in range(s):
    pas.append(int(input()))

l, r = 1, max(pas)
pa = 0

while (l <= r):
    m = (l + r) // 2
    count = 0

    for x in pas:
        count += x // m

    if count >= c:
        l = m + 1
        pa = max(m, pa)
    else: r = m - 1

ans = sum(pas) - (c*pa)

print(ans)