class WordPattern:

    def __init__(self, pattern, word):
        self.pattern = pattern
        self.word = word

    def isPattern(self, pattern: str, word: str) -> bool:
        split_word = word.split()
        if range(len(pattern)) != range(len(split_word)):
            return False
        hash_map = {}
        for i in range(len(pattern)):
            curr_char = pattern[i]
            if curr_char in hash_map:
                if hash_map[curr_char] != split_word[i]:
                    return False
            else:
                if split_word[i] in hash_map.values():
                    return False

            hash_map[curr_char] = split_word[i]
        return True


pattern = "abbac"
word = "dog cat cat dog mouse"
sol = WordPattern(pattern, word)
isTrue = sol.isPattern(pattern, word)
print(isTrue)
