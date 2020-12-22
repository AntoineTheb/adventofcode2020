from copy import deepcopy
import numpy as np


def main():

    def kernel(data, i, j):
        x, y = zip(*[
            [-1, -1],
            [-1, 0],
            [-1, 1],
            [0, -1],
            # [0, 0],
            [0, 1],
            [1, -1],
            [1, 0],
            [1, 1]
        ])
        return data[i + np.array(x), j + np.array(y)]

    def seat_unseat(data):

        def handle(seat, surrounding):
            if seat == 'L':
                occupied = list(surrounding).count('#')
                if occupied == 0:
                    return '#'
            elif seat == '#':
                occupied = list(surrounding).count('#')
                if occupied >= 4:
                    return 'L'
            return seat

        new_data = deepcopy(data)
        X, Y = data.shape

        for i in range(1, X-1):
            for j in range(1, Y-1):
                seat = data[i, j]
                surrounding = kernel(data, i, j)
                new_data[i, j] = handle(seat, surrounding)

        return new_data

    data = []
    with open('input.txt', 'r') as fil:
        line = fil.readline().strip()
        length = len(line)
        data.append([' '] * (length + 2))
        data.append([' '] + list(line) + [' '])
        while line:
            line = fil.readline().strip()
            if len(line) > 0:
                data.append([' '] + list(line) + [' '])

        data.append([' '] * (length + 2))

    data = np.asarray(data)
    new_data = seat_unseat(data)
    count = 1
    while not (data == new_data).all():
        data = new_data
        new_data = seat_unseat(data)
        count += 1
        print('Iteration', count)

    occupado = 0
    for row in new_data:
        occupado += list(row).count('#')
    print(occupado)


if __name__ == "__main__":
    main()
