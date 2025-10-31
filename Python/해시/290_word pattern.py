class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        chars = list(pattern)
        words = s.split(" ")

        if len(chars) != len(words): return False

        char_to_word = {}
        word_to_char = {}

        for c, w in zip(chars, words):
            # dict 안에 이미 값이 있고 그 값이랑 w 값이 다르면 무조건 False
            if c in char_to_word and char_to_word[c] != w: return False
            
            # dict 안에 이미 값이 있고 그 값이랑 c 값이 다르면 무조건 False
            if w in word_to_char and word_to_char[w] != c: return False

            # dict 에다가 값 추가
            char_to_word[c] = w
            word_to_char[w] = c

        return True