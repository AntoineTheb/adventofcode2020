def main():

    count = 0
    lin = 1
    col = 0

    with open('input.txt', 'r') as fil:
        line = fil.readline()
        line = list(line)
        if line[col] == '#':
            count += 1
            line[col] = 'X'
        else:
            line[col] = 'O'
        col += 3
        col = col % (len(line) - 1)
        print(''.join(map(str, line)))
        while line:
            line = fil.readline()
            if len(line) == 0:
                break

            line = list(line)
            print(len(line), col)
            if line[col] == '#':
                count += 1
                line[col] = 'X'
            else:
                line[col] = 'O'
            print(''.join(map(str, line)))
            col += 3
            col = col % (len(line) - 1)
            lin += 1
        print(count)


if __name__ == "__main__":
    main()
