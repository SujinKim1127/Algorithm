t = int(input())

for _ in range(t):
    n = int(input())
    zero = 1
    one = 0
    for i in range(n):
        zero, one = one, zero + one
    print(zero, one)
