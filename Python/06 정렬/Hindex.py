citations = [1,6,7,8,9]
# 1
def solution(citations):
    citations.sort(reverse=True)
    for i in range(len(citations)):
        print(i, citations[i])
        if citations[i] < i + 1:
            print("----if----", citations[i], i)
            return i
    return len(citations)

solution(citations)

# 2
def solution(citations):
    citations.sort()
    l = len(citations)
    for i in range(l):
        print(i, citations[i], l-i)
        if citations[i] >= l-i:
            print("----if----", citations[i], i, l-i)
            return l-i
    return 0

solution(citations)

