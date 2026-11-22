def anti_vowel(text):
    result = []
    for char in text:
        if char.lower() not in "aeiou":
            result.append(char)
    return "".join(result)
