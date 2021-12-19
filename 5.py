from re import fullmatch


def fullrange(start, end):
    dir = 1 if start <= end else -1
    return range(start, end + dir, dir)



def apply_lines_rules(field, rules, diag=False):
    for rule in rules:
        if rule[0] == rule[2]:
            x = rule[0]
            for y in fullrange(rule[1], rule[3]):
                field[x][y] += 1
        elif rule[1] == rule[3]:
            y = rule[1]
            for x in fullrange(rule[0], rule[2]):
                field[x][y] += 1
        elif diag:
            range_x = list(fullrange(rule[0], rule[2]))
            range_y = list(fullrange(rule[1], rule[3]))
            if len(range_x) != len(range_y):
                print(f"Skipping {rule}")
            else:
                for i in range(len(range_x)):
                    field[range_x[i]][range_y[i]] += 1
        else:
            print(f"Skipping {rule}")


def main(args):
    rules = []
    with open("5.txt", "r") as input_file:
        for line in input_file:
            if len(line.strip()) == 0:
                continue
            match = fullmatch("([0-9]+),([0-9]+) -> ([0-9]+),([0-9]+)",
                              line.strip())
            if match is None:
                raise Exception(f"Invalid line: {line}")
            rules.append(
                (int(match.group(1)), int(match.group(2)),
                 int(match.group(3)), int(match.group(4))))
    bounds = max([max(x) for x in rules]) + 1
    field = []
    for i in range(bounds):
        field += [[0] * bounds]
    apply_lines_rules(field, rules, True)
    duplicates = 0
    for row in field:
        for cell in row:
            if cell > 1:
                duplicates += 1
    print(f"Result: {duplicates}")


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))
