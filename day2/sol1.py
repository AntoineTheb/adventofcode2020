import numpy as np


def main():

    def password_validator(line):
        if len(line) > 0:
            beg, password = line.split(':')
            count, letter = beg.split(' ')
            min_l, max_l = map(int, count.split('-'))

            actual = password.count(letter)

            if actual >= min_l and actual <= max_l:
                return True
        return False

    count = 0

    with open('input.txt', 'r') as fil:
        line = fil.readline()
        valid = password_validator(line)
        count += int(valid)
        while line:
            line = fil.readline()
            valid = password_validator(line)
            count += int(valid)

    print(count)

if __name__ == "__main__":
    main()
