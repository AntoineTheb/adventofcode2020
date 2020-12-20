def main():

    def custom_validator(line):
        letters = set(line.replace(' ', ''))
        persons = line.strip().split(' ')
        count = 0
        for letter in sorted(letters):
            mask = [p.find(letter) for p in persons]
            if -1 not in mask:
                count += 1
        return count

    count = 0
    with open('input.txt', 'r') as fil:
        line = fil.readline()
        full = line[:-1]
        while line:
            if len(line) == 1:
                count += int(custom_validator(full))
                full = ''

            line = fil.readline()
            full += line[:-1] + ' '

        count += int(custom_validator(full))

    print(count)


if __name__ == "__main__":
    main()
