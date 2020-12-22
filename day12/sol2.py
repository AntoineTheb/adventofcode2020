
def main():

    x, y = 0, 0
    wx, wy = 10, 1

    def moving(cmd, val, x, y, wx, wy):
        if cmd == 'N':
            wy += val
        elif cmd == 'E':
            wx += val
        elif cmd == 'S':
            wy -= val
        elif cmd == 'W':
            wx -= val
        elif cmd == 'F':
            x += wx * val
            y += wy * val
        elif cmd == 'L':
            new_x = (val // 90) % 4

            if new_x == 1:
                t = wx
                wx = -wy
                wy = t
            if new_x == 2:
                wx, wy = -wx, -wy
            if new_x == 3:
                t = wx
                wx = wy
                wy = -t

        elif cmd == 'R':
            new_x = (val // 90) % 4

            if new_x == 1:
                t = wx
                wx = wy
                wy = -t
            if new_x == 2:
                wx, wy = -wx, -wy
            if new_x == 3:
                t = wx
                wx = -wy
                wy = t

        return x, y, wx, wy

    with open('input.txt', 'r') as fil:
        line = fil.readline().strip()
        cmd, val = line[0], line[1:]
        print(cmd, val)
        x, y, wx, wy = moving(
            cmd, int(val), x, y, wx, wy)
        print(x, y, wx, wy)
        while line:
            line = fil.readline().strip()
            if len(line) > 0:
                cmd, val = line[0], line[1:]
                print(cmd, val)
                x, y, wx, wy = moving(
                    cmd, int(val), x, y, wx, wy)
                print(x, y, wx, wy)

    print(x, y, wx, wy)
    print(abs(x) + abs(y))


if __name__ == "__main__":
    main()
