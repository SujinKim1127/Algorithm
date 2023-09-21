n = int(input())

array = []

for _ in range(n):
    array.append(list(input().split()))

def setting(data):
    return int(data[0])

result = sorted(array, key=setting)

for i in range(n):
    for x in result[i]:
        print(x, end=' ')
    print()