def main():

    def custom_validator(line):
        return len(set(line))

    count = 0
    with open('input.txt', 'r') as fil:
        line = fil.readline()
        full = line[:-1]
        while line:
            if len(line) == 1:
                count += int(custom_validator(full))
                full = ''

            line = fil.readline()
            full += line[:-1] + ''

        count += int(custom_validator(full))

    print(count)


if __name__ == "__main__":
    main()
