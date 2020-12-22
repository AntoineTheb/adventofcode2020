from collections import defaultdict
import numpy as np


def main():

    data = sorted(np.loadtxt('input.txt'))

    data = [0] + data + [data[-1] + 3]

    coming = defaultdict(int)
    coming[0] = 1

    for adapter in data[1:]:
        coming[adapter] = sum([coming[adapter - i] for i in range(1, 4)])

    print(coming[data[-1]])

if __name__ == "__main__":
    main()
