def main():

    def seat_id(instructions):
        rows = list(range(0, 128))
        cols = list(range(0, 8))

        for i in instructions:
            med_row = len(rows) // 2
            med_col = len(cols) // 2

            if i == 'F':
                rows = rows[:med_row]
            elif i == 'B':
                rows = rows[med_row:]
            elif i == 'L':
                cols = cols[:med_col]
            elif i == 'R':
                cols = cols[med_col:]
            else:
                assert False

        return (rows[0] * 8) + cols[0]

    seat_ids = []
    with open('input.txt', 'r') as fil:
        line = fil.readline().strip()
        seat = seat_id(line)
        seat_ids.append(seat)
        while line:
            line = fil.readline().strip()
            seat = seat_id(line)
            seat_ids.append(seat)

    sorted_list = sorted(seat_ids)[1:]
    true_ids = list(range(48, 875))

    print(sorted_list, true_ids)

    for actual, theo in zip(sorted_list, true_ids):
        if actual != theo:
            print(actual, theo)
            break


if __name__ == "__main__":
    main()
