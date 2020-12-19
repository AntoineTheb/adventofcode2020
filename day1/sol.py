import numpy as np

from itertools import combinations


def main():

    data = np.loadtxt('input.txt')

    for comb in combinations(data, 2):
        one, two = comb
        # print(one, two, one + two)
        if one + two == 2020.0:
            print(one * two)


if __name__ == "__main__":
    main()
