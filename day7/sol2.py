from collections import defaultdict


def main():

    def handle_line(line):
        """ Return which bags can be contained by which
        """
        split = line.split('contain')

        outer = ''.join(split[0].split(' ')[:2])
        bags = {outer: []}
        inner = [s.strip().split(' ') for s in split[1].split(',')]
        if inner[0][0] == 'no':
            return bags
        else:
            for bag in inner:
                number = int(bag[0])
                color = ''.join(bag[1:3])
                bags[outer].append((number, color))

        return bags

    with open('input.txt', 'r') as fil:
        line = fil.readline().strip()
        contains = defaultdict(lambda: [])

        dicts = handle_line(line)

        for c in dicts.keys():
            for cprime in dicts[c]:
                contains[c].append(cprime)

        while line:
            line = fil.readline().strip()
            if len(line) == 0:
                break
            dicts = handle_line(line)

            for c in dicts.keys():
                for cprime in dicts[c]:
                    contains[c].append(cprime)

    allchildren = []
    children = []
    for nb, c in contains['shinygold']:
        allchildren += nb * [c]
        children += nb * [c]

    while len(children) > 0:
        new_children = []
        for c in children:
            # print(len(contains[c]))
            for nb, nc in contains[c]:
                allchildren += nb * [nc]
                new_children += nb * [nc]
        children = new_children
        # print(children)

    print(len(allchildren))


if __name__ == "__main__":
    main()
