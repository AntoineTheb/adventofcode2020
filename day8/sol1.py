def main():

    instructions = []
    accumulator = 0
    index = 0

    def handle_line(line, index, accumulator):

        program = {
            'acc': lambda acc, value: (index + 1, accumulator + value),
            'jmp': lambda acc, value: (index + value, accumulator),
            'nop': lambda acc, value: (index + 1, accumulator)
        }

        inst, val = line.split(' ')
        print(inst, val)
        return program[inst](accumulator, int(val))

    with open('test_input.txt', 'r') as fil:
        line = fil.readline().strip()
        instructions += [line]
        while True:
            line = fil.readline().strip()
            if len(line) > 0:
                instructions += [line]
            else:
                break

    visited = []

    while True:
        new_index, new_accumulator = handle_line(
            instructions[index], index, accumulator)
        if new_index not in visited:
            index = new_index
            visited += [index]
            accumulator = new_accumulator
        else:
            break

    print(accumulator)


if __name__ == "__main__":
    main()
