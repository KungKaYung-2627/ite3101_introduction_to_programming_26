def reverse(text):
    result = []
    for index in range(len(text) - 1, -1, -1):
        result.append(text[index])
    return "".join(result)
