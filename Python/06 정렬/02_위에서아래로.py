n = int(input())

number = []

for _ in range(n):
    number.append(int(input()))

number.sort(reverse=True)

for x in number:
    print(x, end=" ")