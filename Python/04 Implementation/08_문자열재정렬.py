import re

str = input()
numbers = list(map(int, re.findall(r'\d', str)))
alpha = list(re.sub(r"[0-9]", '', str))
print(numbers)
print(alpha)
strsum = "{}".format(sum(numbers))

alpha.sort()
result = ''.join(alpha)
print(result,strsum, sep='')
