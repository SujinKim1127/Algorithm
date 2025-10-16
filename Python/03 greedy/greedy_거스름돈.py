n = int(input())

money = [500, 100, 50, 10]
cnt = 0

for coin in money:
    cnt += n // coin
    n %= coin    

print(cnt)
