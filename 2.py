from re import match as do_match


def main(args):
    withaim = True
    aim = 0
    down = 0
    forward = 0
    with open("2.txt", "r") as input_file:
        for line in input_file:
            match = do_match("(up|down|forward) ([0-9]+)", line.strip())
            if match is None:
                raise Exception(f"Invalid line '{line}'")
            val = int(match.group(2))
            op = match.group(1)
            if op == "up":
                if withaim:
                    aim -= val
                else:
                    down -= val
            elif op == "down":
                if withaim:
                    aim += val
                else:
                    down += val
            elif op == "forward":
                forward += val
                if withaim:
                    down += (aim * val)
            else:
                raise Exception(f"Invalid direction '{op}'")
        print(f"Down {down}, Forward {forward}, Res: {down * forward}")


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))
