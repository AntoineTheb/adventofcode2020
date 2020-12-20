from itertools import combinations

import numpy as np


def main():

    data = np.loadtxt('input.txt', dtype=np.int)

    valid = True
    pre_beg = 0
    pre_end = 25
    while valid:
        preample = data[pre_beg:pre_end]
        is_valid = False
        for one, two in combinations(preample, 2):
            if one + two == data[pre_end]:
                is_valid = True
                break
        valid = is_valid
        pre_beg += 1
        pre_end += 1

    print(data[pre_end-1])


if __name__ == "__main__":
    main()
