n = [3, 5, 7]


def double_list(x):
    for i in range(len(x)):
        x[i] *= 2
    return x


# A second call doubles the same list again because it was changed in place.
double_list(n)
print(double_list(n))
