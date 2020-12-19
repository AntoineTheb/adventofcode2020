required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
cid = 'cid'


def main():

    def value_validator(key, val):

        def int_val(minv, maxv, value):
            intv = int(value)
            return intv >= minv and intv <= maxv

        def height_val(value):
            height_valid = False
            if value[-2:] == 'cm':
                height_valid = int_val(150, 193, value[:-2])
            elif value[-2:] == 'in':
                height_valid = int_val(59, 76, value[:-2])
            return height_valid

        def hair_val(value):
            if value[0] != '#':
                return False
            for v in value[1:]:
                if v not in '0123456789abcdef':
                    return False
            return True

        def eye_color(value):
            if value not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                return False
            return True

        def pid_val(value):
            for v in value:
                if v not in '0123456789' or len(value) != 9:
                    return False
            return True

        valid = True
        if key == 'byr':
            valid = int_val(1920, 2002, val)
        elif key == 'iyr':
            valid = int_val(2010, 2020, val)
        elif key == 'eyr':
            valid = int_val(2020, 2030, val)
        elif key == 'hgt':
            valid = height_val(val)
        elif key == 'hcl':
            valid = hair_val(val)
        elif key == 'ecl':
            valid = eye_color(val)
        elif key == 'pid':
            valid = pid_val(val)
        elif key == 'cid':
            pass
        return valid

    def passport_validator(line):
        valid = True
        properties = line.strip().split(' ')
        keyvals = [prop.split(':') for prop in properties]
        keys, _ = zip(*keyvals)
        missing = []
        for req in required:
            if req not in keys:
                missing.append(req)
                valid = False
            if valid:
                for key, val in keyvals:
                    val_valid = value_validator(key, val)
                    if not val_valid:
                        print(key, val)
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
