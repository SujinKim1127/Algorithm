class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        answer = ""
        for first, second in zip(word1, word2):
            print(first, second)
            answer += first + second
        
        return answer + word1[len(word2):] + word2[len(word1):]