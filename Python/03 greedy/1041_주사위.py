# 풀이 1
n = int(input())
arr = list(map(int, input().split()))
minArr= []

answer = 0
if n == 1: 
    arr.sort()
    answer = sum(arr[:5])
else: 
    minArr.append(min(arr[0], arr[5]))
    minArr.append(min(arr[1], arr[4]))
    minArr.append(min(arr[2], arr[3]))
    minArr.sort()


    answer += minArr[0] * (n * n *2 + n*(n-2)*2 + (n-2)*(n-2))
    answer += minArr[1] * (n * 4 + (n-2)*4)
    answer += minArr[2] * 4


print(answer)
        
# 풀이 2
n = int(input())
arr = list(map(int, input().split()))
minArr= []

answer = 0
if n == 1: 
    arr.sort()
    answer = sum(arr[:5])
else: 
    minArr.append(min(arr[0], arr[5]))
    minArr.append(min(arr[1], arr[4]))
    minArr.append(min(arr[2], arr[3]))
    minArr.sort()

    # 1 2 3 개의 면의 최소값
    min1 = minArr[0]    # 1면만 보이니까
    min2 = minArr[0] + minArr[1]    # 2개의 면만 보이니까
    min3 = minArr[0] + minArr[1] + minArr[2]    # 3개의 면이 보이니까

    
    n1 = (n-2)*(n-2)*5 + (n-2)*4
    n2 = 4*(n-2) + 4*(n-1)
    n3 = 4

    answer += n1 * min1
    answer += n2 * min2
    answer += n3 * min3


print(answer)