required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
cid = 'cid'


def main():

    def passport_validator(line):
        valid = True
        properties = line.strip().split(' ')
        keys = [prop.split(':')[0] for prop in properties]
        missing = []
        for req in required:
            if req not in keys:
                missing.append(req)
                valid = False
        if not valid:
            print(line.strip(), missing)
        return valid

    count = 0

    with open('input.txt', 'r') as fil:
        line = fil.readline()
        full = line[:-1]
        while line:
            if len(line) == 1:
                count += int(passport_validator(full))
                full = ''

            line = fil.readline()
            full += line[:-1] + ' '

        count += int(passport_validator(full))

    print(count)


if __name__ == "__main__":
    main()
