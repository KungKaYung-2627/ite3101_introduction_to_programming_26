def count(sequence, item):
    total = 0
    for value in sequence:
        if value == item:
            total += 1
    return total
