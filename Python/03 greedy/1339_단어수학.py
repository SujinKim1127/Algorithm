n = int(input())
alphabet_dict = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'J':0, 'K':0, 'L':0, 'M':0, 'N':0, 'O':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'U':0, 'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0}

alpha = []
for _ in range(n):
    alpha.append(input())

# 알파벳에 자리값 숫자 더해주기
for x in alpha:
    for i in range(len(x)):
        num = 10 ** (len(x) - 1 - i)
        alphabet_dict[x[i]] += num

value = []
for x in alphabet_dict.values():
    if x > 0: value.append(x)

value.sort(reverse=True)
answer = 0
for x in range(len(value)):
    answer += value[x] * (9-x)

print(answer)
