n = int(input())

# student = []
# for _ in range(n):
#     data = input().split()
#     data.reverse()
#     student.append(data)

# student.sort()

# for i in range(len(student)):
#     print(student[i][1], end=" ")

array = []
for i in range(n):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1])))

array = sorted(array, key=lambda student: student[1])
print(array)

for student in array:
    print(student[0], end=' ')