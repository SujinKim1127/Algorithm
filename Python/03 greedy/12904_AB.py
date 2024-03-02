S = input()
T = input()

for _ in range(0, len(T) - len(S)):
    last = T.strip()[-1]
    if last == 'B':
        T = T[:-1]      # 마지막 문자 B 삭제
        T = T[::-1]     # 뒤집기
    else:
        T = T[:-1]      # 마지막 문자 A 삭제

if T == S: print(1)
else: print(0)