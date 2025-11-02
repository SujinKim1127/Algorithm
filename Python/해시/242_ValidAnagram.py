class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashT = {}
        for x in t:
            hashT[x] = hashT.get(x, 0) + 1
        
        for x in s:
            if hashT.get(x, 0) == 0: return False
            hashT[x] -= 1
        
        for x in t:
            if hashT.get(x, 0) > 0: return False

        return True
    
    # 연산속도가 더 빠른 .count() 함수
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        for c in set(t):
            if t.count(c) > s.count(c): return False
        
        return True