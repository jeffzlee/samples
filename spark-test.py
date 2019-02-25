from operator import add
def tokenize(text):
    return text.split()
words = text.flatMap(tokenize)
print words
