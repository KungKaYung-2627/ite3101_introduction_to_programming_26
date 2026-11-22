def censor(text, word):
    words = text.split()
    for index in range(len(words)):
        if words[index] == word:
            words[index] = "*" * len(word)
    return " ".join(words)
