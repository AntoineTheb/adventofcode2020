def main():

    facing = ['N', 'E', 'S', 'W']
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    direction = 'E'

    x, y = 0, 0

    def moving(cmd, val, x, y, direction):
        if cmd == 'N':
            return x, y+val, direction
        if cmd == 'E':
            return x+val, y, direction
        if cmd == 'S':
            return x, y-val, direction
        if cmd == 'W':
            return x-val, y, direction
        if cmd == 'F':
            dx, dy = directions[facing.index(direction)]
            dx *= val
            dy *= val
            return x + dx, y + dy, direction
        if cmd == 'L':
            direction = facing[(facing.index(direction) - (val // 90)) % len(directions)]
            return x, y, direction
        if cmd == 'R':
            direction = facing[(facing.index(direction) + (val // 90)) % len(directions)]
            return x, y, direction

    with open('input.txt', 'r') as fil:
        line = fil.readline().strip()
        cmd, val = line[0], line[1:]
        print(cmd, val)
        x, y, direction = moving(cmd, int(val), x, y, direction)
        print(x,y,direction)
        while line:
            line = fil.readline().strip()
            if len(line) > 0:
                cmd, val = line[0], line[1:]
                print(cmd, val)
                x, y, direction = moving(cmd, int(val), x, y, direction)
                print(x,y,direction)

    print(x, y, direction)
    print(abs(x) + abs(y))


if __name__ == "__main__":
    main()
