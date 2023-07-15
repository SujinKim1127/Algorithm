n = int(input())

# n3초: 6 * 60
# 3n초: 10 * 60
s = 6*60 + 10 * 60 - 60
# n3분: 6 * 60 - 6 * 6
# 3n분: 10 * 60
m = 6 * 60 - 6 * 6 + 10 * 60 - 60


ms = s + m

h = 60 * 60


# if(n < 3):
#     print(n * ms)
# elif(n < 13 | n >= 3):
#     print(h+(n-1)*ms)
# elif(n < 23 | n >= 13):
#     print(h*2 + (n-2)*ms)
# else:
#     print(h*3 + (n-3)*ms)
cnt = 0
for h in range(n+1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h) + str(m) + str(s):
                cnt += 1

print(cnt)