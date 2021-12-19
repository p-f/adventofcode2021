import math


def main(args):
    window_size = 3
    previous = []
    current = []
    res = 0
    with open("1.txt", "r") as input_file:
        for line in input_file:
            nr = int(line)
            current += [nr]
            current = current[-window_size:]
            if current != previous and len(current) == window_size and\
                    len(previous) == window_size:
                if sum(current) > sum(previous):
                    res += 1
            previous = list(current)
    print(f"Result: {res}")


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))
