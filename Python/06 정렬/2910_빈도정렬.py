import collections

n, c = map(int, input().split())
mesg = list(map(int, input().split()))

cnt = {}

for i in mesg:
    if i not in cnt:
        cnt[i]=0
    cnt[i] += 1

print("before", cnt)
frequency=collections.Counter(cnt) 

print("frequnecy", frequency)

# 정렬
cnt=sorted(cnt.items(), key=lambda x: x[1], reverse=True)

l=sorted(l,key=lambda x:(-frequency[x],l.index(x))) 

print("after", cnt)

# 갯수만큼 반복 출력
for key, value in cnt:
    for i in range(value):
        print(str(key), end=" ")