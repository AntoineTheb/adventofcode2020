import numpy as np


def main():

    data = sorted(np.loadtxt('input.txt'))

    ones, threes = np.unique(np.diff([0] + data + [data[-1] + 3]),
                             return_counts=True)[1]

    print(ones * threes)


if __name__ == "__main__":
    main()
