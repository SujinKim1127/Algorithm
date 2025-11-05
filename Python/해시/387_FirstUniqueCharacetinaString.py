from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = {}
        for char in s:
            hashmap[char] = hashmap.get(char, 0) + 1
        # print(hashmap)

        for i, char in enumerate(s):
            if hashmap.get(char, 0) == 1: return i
        
        # Counter 함수로 풀기
        freq = Counter(s)
        for i ,char in enumerate(s):
            if freq[char] == 1: return i

        return -1