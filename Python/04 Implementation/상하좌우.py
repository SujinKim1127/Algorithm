n = int(input())
route = list(input().split())

R = (0, +1)
U = (-1, 0)
D = (+1, 0)
L = (0, -1)

map = [[0 for j in range(n)] for i in range(n)]
present = [1, 1]
for i in route:
    if (i == 'R'):
        if(present[1] + 1 > n): continue
        else: present[1] += 1
    elif(i == 'U'):
        if(present[0] - 1 <= 0): continue
        else: present[0] -= 1
    elif(i == 'D'):
        if(present[0] + 1 > n): continue
        else: present[0] += 1
    elif(i == 'L'):
        if(present[1] - 1 <= n): continue
        else: present[1] -= 1

x = present[0]
y = present[1]

print(x, y)