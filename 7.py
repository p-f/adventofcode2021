import math
from statistics import median

from common import read_tokens


def get_cost(positions: list[int], position: int) -> int:
    return sum([abs(p - position) for p in positions])


def get_cost_nonlinear(positions: list[int], position: int) -> int:
    def _cost(pos: int) -> int:
        diff = abs(pos - position)
        cst = int((diff * (diff + 1)) / 2)
        return cst

    return sum([_cost(p) for p in positions])


def main(args):
    pos: list[int] = read_tokens("7.txt", int)
    median_pos = int(median(pos))
    print(f"Median={median_pos}")
    for offset in range(median_pos - 3, median_pos + 4, 1):
        print(f"Pos: {offset}, Cost: {get_cost(pos, offset)}")
    print()
    offset_min = -1
    min_cost = math.inf
    for offset in range(min(pos), max(pos) + 1):
        cost = get_cost_nonlinear(pos, offset)
        if cost < min_cost:
            offset_min = offset
            min_cost = cost
    print(f"Min at {offset_min}, cost {min_cost}")

    return 0


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))
