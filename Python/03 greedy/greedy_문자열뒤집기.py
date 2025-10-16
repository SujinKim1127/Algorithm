n = list(input())

data = []
zero = 0
one = 0

diff = 0

for i in range(int(len(n)) - 1):
    if(n[i] != n[i+1]) : diff += 1


if(diff % 2 == 0): print(diff // 2)
elif(diff % 2 == 1): print(diff // 2 + 1)


## 답안이랑 풀이가 좀 다름
