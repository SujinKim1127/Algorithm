n, l, w, h = map(int, input().split())

left, right = 0, min(l, w, h)

for _ in range(10000):
    m = (left + right) / 2
    count = (l // m) * (w // m) * (h // m)
    if count >= n:
        left = m
    else: right = m

print("%.10f" %(right))