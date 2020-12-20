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

    weakness = data[pre_end-1]
    print('Found weakness: {}'.format(weakness))

    print('Generating sublists ..')

    # from https://stackoverflow.com/a/47101915
    def all_sublists(L):
        for w in range(1, len(L)+1):
            for i in range(len(L)-w+1):
                yield L[i:i+w]

    print('Got sublists ..')
    print('Verifying additions')

    for sub in all_sublists(data[:pre_end-1]):
        # print(sub, end="\r")
        if sum(sub) == weakness:
            print(min(sub) + max(sub))


if __name__ == "__main__":
    main()
