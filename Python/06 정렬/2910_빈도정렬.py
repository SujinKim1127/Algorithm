n, c = map(int, input().split())

mesg = list(map(int, input().split()))

order = dict.fromkeys(mesg)
order = list(order)

print(order)

count = [0] * (max(mesg) + 1)

for i in range(len(mesg)):    
    count[mesg[i]] += 1

sort_count = []

for i in range(len(count)):
    sort_count.append((i, count[i]))

def sorting(data):
    return data[1]

result = sorted(sort_count, key=sorting,reverse=True)

for x in result:
    if(x[1] > 0):
        for i in range(x[1]):
            print(x[0], end=' ')

