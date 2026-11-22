squares = [x ** 2 for x in range(1, 11)]
print(list(filter(lambda square: 30 <= square <= 70, squares)))
