a = [5, 10, 15, 20, 25]
b = []


def firstlast(x, y):
    length_x = len(x)
    y.append(x[0:1])
    y.append(x[length_x - 1:length_x])


firstlast(a, b)
print(b)
