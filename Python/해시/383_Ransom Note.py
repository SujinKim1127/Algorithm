from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazHash = {}

        for x in magazine: 
            magazHash[x] = magazHash.get(x, 0) + 1

        for x in ransomNote:
            if magazHash.get(x, 0) == 0:
                return False
            magazHash[x] -= 1       # 이미 카운트 한거는 차감하기

        return True
    

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for c in set(ransomNote):
            if ransomNote.count(c) > magazine.count(c): return False
        
        return True
    
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom = Counter(ransomNote)
        magaz = Counter(magazine)
  
        print(ransom)
        print(magaz)
        
        return all(ransom[c] <= magaz[c] for c in ransom )
