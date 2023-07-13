n = list((input()))
n = list(map(int, n))


result = 1
for i in range(len(n)):
    if n[i] <= 1 or result <= 1:
        result += n[i]
    else:
        result *= n[i]

print(result)

## 1일때는 더해줘야한다는 생각 못함