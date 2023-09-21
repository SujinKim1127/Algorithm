s = input()

slice = []
for i in range(len(s)):
    slice.append(s[i:])

result = sorted(slice)

for s in result:
    print(s)
