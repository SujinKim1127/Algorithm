N = int(input())
km = list(map(int, input().split()))
liter = list(map(int, input().split()))

present = liter[0]
total = 0
for x in range(0, N-1):
    present = min(present, liter[x])
    total += present * km[x]
print(total)