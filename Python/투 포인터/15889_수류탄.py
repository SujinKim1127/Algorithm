n = int(input())
people = list(map(int, input().split()))
if n > 1: distance = list(map(int, input().split()))
else: 
    print("권병장님, 중대장님이 찾으십니다")
    exit()

Dmax = 0
for i in range(n-1):
    Dmax = max(Dmax, people[i] + distance[i])

    if Dmax >= people[i+1]: continue
    else: 
        print("엄마 나 전역 늦어질 것 같아")
        exit()

print("권병장님, 중대장님이 찾으십니다")

