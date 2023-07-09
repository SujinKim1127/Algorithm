n = list((input()))
n = list(map(int, n))


result = 1
for i in range(len(n)):
    print(n[i])
    if n[i] != 0:
        result *= n[i]

print(result)