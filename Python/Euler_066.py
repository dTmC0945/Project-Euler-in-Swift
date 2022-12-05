import numpy as np


def perfectSquare(limit):
    array = []
    for value in range(2, int(np.ceil(np.sqrt(limit)))):
        array.append(value ** 2)

    return array


p_squares = perfectSquare(1000)

list = np.arange(2, 1000)

filtered_list = set(list) - set(p_squares)

max_x = 0
max_Value = 0
for D in filtered_list:
    x, y = 1, 1
    while True:
        eq = x ** 2 - D * y ** 2
        if x > 40000:
            break
        if eq > 1:
            y += 1
        elif eq < 1:
            x += 1
        elif eq == 1:

            break

    if x > max_x:
        max_x = x
        max_Value = D

print(D)