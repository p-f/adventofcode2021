def do_step(state):
    new_state = [0 for _ in range(9)]
    for i, nr in enumerate(state):
        if i == 0:
            new_state[6] += nr
            new_state[8] += nr
        else:
            new_state[i - 1] += nr
    return new_state


def main(args):
    state = [0 for _ in range(9)]
    with open("6.txt", "r") as input_file:
        for line in input_file:
            ldata = line.strip()
            if len(ldata) == 0:
                continue
            for c in ldata.split(","):
                age = int(c)
                state[age] += 1
    print(f"Start: {state}")
    for _ in range(256):
        state = do_step(state)
    print(f"Final: {state}, Total: {sum(state)}")


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))
