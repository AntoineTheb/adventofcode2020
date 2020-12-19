def count_trees(right):
    col = 0
    count = 0
    with open('input.txt', 'r') as fil:
        line = fil.readline()
        col += right
        col = col % (len(line) - 1)
        while line:
            line = fil.readline()
            if len(line) == 0:
                break

            if line[col] == '#':
                count += 1
            col += right
            col = col % (len(line) - 1)

    return count


def count_trees_skip(right):
    col = 0
    count = 0
    with open('input.txt', 'r') as fil:
        line = fil.readline()
        col += right
        col = col % (len(line) - 1)
        while line:
            line = fil.readline()
            line = fil.readline()
            if len(line) == 0:
                break

            if line[col] == '#':
                count += 1
            col += right
            col = col % (len(line) - 1)

    return count


def main():

    print(count_trees(3) *
          count_trees(1) *
          count_trees(5) *
          count_trees(7) *
          count_trees_skip(1))


if __name__ == "__main__":
    main()
