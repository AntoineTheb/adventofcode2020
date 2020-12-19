import numpy as np

from itertools import combinations


def main():

    data = np.loadtxt('input.txt')

    for comb in combinations(data, 3):
        one, two, three = comb
        # print(one, two, one + two)
        if one + two + three == 2020.0:
            print(one * two * three)


if __name__ == "__main__":
    main()
