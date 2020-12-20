from copy import deepcopy


def main():

    instructions = []

    def handle_line(inst, val, index, accumulator):

        program = {
            'acc': lambda acc, value: (index + 1, accumulator + value),
            'jmp': lambda acc, value: (index + value, accumulator),
            'nop': lambda acc, value: (index + 1, accumulator)
        }

        return program[inst](accumulator, int(val))

    with open('input.txt', 'r') as fil:
        line = fil.readline().strip()
        instructions += [line.split(' ')]
        while True:
            line = fil.readline().strip()
            if len(line) > 0:
                instructions += [line.split(' ')]
            else:
                break

    for i in range(len(instructions)):
        accumulator = 0
        index = 0
        modified = deepcopy(instructions)
        visited = []
        infinite = False

        if modified[i][0] == 'jmp':
            modified[i][0] = 'nop'
        elif modified[i][0] == 'nop':
            modified[i][0] = 'jmp'

        while not infinite and index < len(modified):
            inst, val = modified[index]
            new_index, new_accumulator = handle_line(
                inst, val, index, accumulator)
            if new_index not in visited:
                index = new_index
                visited += [index]
                accumulator = new_accumulator
            else:
                infinite = True

        if not infinite:
            print(accumulator)


if __name__ == "__main__":
    main()
