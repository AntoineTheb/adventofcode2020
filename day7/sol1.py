from collections import defaultdict


def main():

    def handle_line(line):
        """ Return which bags can be contained by which
        """
        bags = {}
        colors = []
        split = line.split('contain')

        outer = ''.join(split[0].split(' ')[:2])
        colors.append(outer)
        inner = [s.strip().split(' ') for s in split[1].split(',')]
        if inner[0][0] == 'no':
            return colors, {}
        else:
            for bag in inner:
                color = ''.join(bag[1:3])
                bags[color] = [outer]
                colors.append(color)

        return colors, bags

    with open('input.txt', 'r') as fil:
        line = fil.readline().strip()
        contained_by = defaultdict(lambda: [])

        colors, dicts = handle_line(line)

        for c in dicts.keys():
            for cprime in dicts[c]:
                contained_by[c].append(cprime)

        set_colors = set(colors)

        while line:
            line = fil.readline().strip()
            if len(line) == 0:
                break
            colors, dicts = handle_line(line)

            for c in colors:
                set_colors.add(c)

            for c in dicts.keys():
                for cprime in dicts[c]:
                    contained_by[c].append(cprime)

        parents = contained_by['shinygold']
        new_parents = []
        while True:
            for p in parents:
                for np in contained_by[p]:
                    if np not in parents and np not in new_parents:
                        new_parents.append(np)
            parents += new_parents
            if len(new_parents) == 0:
                break
            new_parents = []

        print(parents)
        print(len(parents))


if __name__ == "__main__":
    main()
