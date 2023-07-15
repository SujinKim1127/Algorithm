row = ['a', 'b', 'c', 'd','e','f','g','h']
col = [1,2,3,4,5,6,7,8]

pos = list(input())

nx = row.index(pos[0])
ny = col.index(int(pos[1]))


cnt = 0

if(
nx - 1 >= 0 and
ny - 2 >= 0 ):
    cnt += 1

if(
nx + 1 <= 7 and
ny - 2 >=0 ):
    cnt += 1

if(
nx - 2 >=0 and
ny - 1 >= 0 ):
    cnt += 1

if(
nx + 2 <= 7 and
ny - 1 >= 0 ):
    cnt += 1

if(
nx - 2 >=0 and
ny + 1 <= 7 ):
    cnt += 1

if(
nx + 2 <= 7 and
ny + 1 <= 7 ):
    cnt += 1

if(
nx - 1 >= 0 and
ny + 2 <= 7 ):
    cnt += 1

if(
nx + 1 <= 7 and
ny + 2 <= 7 ):
    cnt += 1




print(cnt)


### answer
steps = [
    (-2, -1), (-1, -2), (1, -2), (2, -1),
    (2, 1), (1, 2), (-1, 2), (-2, 1)
]

result = 0
for step in steps:
    next_row = nx+1 + step[0] 
    next_col = ny+1 + step[1]

    if(next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8):
        result += 1

print(result)