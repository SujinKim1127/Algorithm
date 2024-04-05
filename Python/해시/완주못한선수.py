# 해시 테이블 사용한 풀이
def solution(participant, completion):
    answer = {}
    for i in participant:
        answer[i] = answer.get(i, 0) + 1
    for j in completion:
        answer[j] -= 1
    for k in answer:
        print(k, answer[k])
        if answer[k]: return k

# 해시 함수 사용 풀이
def solution(participant, completion):
    value = 0
    answer = {}
    for part in participant:
        answer[hash(part)] = part
        value += int(hash(part))

    for comp in completion:
        value -= hash(comp)

    return answer[value]

