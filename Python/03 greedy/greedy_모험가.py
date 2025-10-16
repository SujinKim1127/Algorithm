n = int(input())
data = list(map(int, input().split()))

data.sort(reverse=True)  # 내림차순

result = 0
while ( len(data) >= data[0] ):
    del data[0:data[0]]
    result += 1
    if(len(data) == 0): break

print(result)


# answer
# n = int(input())
# data = list(map(int, input().split()))
# data.sort()

# result = 0
# count = 0

# for i in data:
#     count += 1
#     if count > i:
#         result += 1
#         count = 0

# print(result)