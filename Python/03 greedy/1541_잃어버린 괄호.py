text = input()
arr = text.split('-')

answer = 0
first = arr[0].split('+')
for i in first:
    answer += int(i)

for x in range(1, len(arr)):
    num = arr[x].split('+')
    for i in num:
        answer -= int(i)

print(answer)