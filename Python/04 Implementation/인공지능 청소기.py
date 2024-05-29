t = int(input())
for _ in range(t):
	x, y, n = map(int, input().split())
	sum = abs(x) + abs(y)
	if (sum % 2 == n % 2 and (sum <= n)):
		print("YES")
	else:
		print("NO")
