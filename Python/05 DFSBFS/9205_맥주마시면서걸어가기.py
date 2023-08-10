t = int(input())
for i in range(t):
    n = int(input())        # 맥주 파는 편의점 개수
    house = list(map(int, input().split()))
    store = []
    for _ in range(n):
        store.append(list(map(int, input().split())))
    rock = list(map(int, input().split()))




print(house, store, rock)


