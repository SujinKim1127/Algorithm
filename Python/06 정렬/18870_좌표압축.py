n = int(input())
arr = list(map(int, input().split()))
sortArr = sorted(set(arr))
dic = { sortArr[i]:i for i in range(len(sortArr))}
for x in arr:
    print(dic[x], end=" ")
