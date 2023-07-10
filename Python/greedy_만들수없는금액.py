n = int(input())

data = list(map(int, input().split(' ')))

money = []

for i in range(n):
    money.append(data[i])

money.sort()

result = 1

for x in money:
    if result < x:
        break
    else:
        result += x
print(result)