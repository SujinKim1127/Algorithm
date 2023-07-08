n = int(input())

data = list(map(int, input().split()))

data.sort(reverse=True)

result = 0
while ( len(data) > 0 ):
    del data[0:data[0]]
    result += 1

print(result)