def solution(s):
    cnt = 0
    arr = list(s)
    for x in arr:
        if x == '(': cnt += 1
        else:
            if cnt > 0: cnt -= 1
            else: return False
        
    if cnt == 0: return True
    else: return False


# stack으로 푸는 법
def solution(s):
    stack = []
    for x in s:
        if x == '(': stack.append(x)
        else:
            try: stack.pop()
            except: return False
        
    return len(stack) == 0

