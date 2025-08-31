class Word:
    def __init__ (self, word):
        self.word = word

    def __lt__ (self, other):
        return self.word + other.word < other.word + self.word


n = int(input())
strings = []
for _ in range(n):
    strings.append(Word(input().strip("\n")))

strings.sort()
for word in strings:
    print(word.word, end = "")
