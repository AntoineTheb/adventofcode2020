import numpy as np


def main():

    def password_validator(line):
        if len(line) > 0:
            beg, password = line.split(':')
            password = password[1:]
            count, letter = beg.split(' ')
            first_pos, second_pos = map(int, count.split('-'))

            a = password[first_pos-1] == letter
            b = password[second_pos-1] == letter
            if (a and not b) or (not a and b):
                return True
            print(first_pos-1, second_pos-1, password[first_pos-1], password[second_pos-1], letter, password)
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
