n = list(input())

if(len(n) % 2 != 0): print(False)

half = len(n) // 2
first = map(int, n[0:half])
second = map(int, n[half:len(n)+1])

if(sum(first) == sum(second)): print("LUCKY")
else: print("READY")