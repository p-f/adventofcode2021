def get_characteristic(lines, default=None):
    state = [0] * len(lines[0])
    for line in lines:
        line_data = line.strip()
        for c in range(len(line_data)):
            if line_data[c] == '0':
                state[c] -= 1
            elif line_data[c] == '1':
                state[c] += 1
            else:
                raise Exception(f"Invalid line '{line_data}', pos {c}")
    result_binary = ""
    result_inv = ""
    for s in state:
        if s < 0:
            result_binary += "0"
            result_inv += "1"
        elif s > 0:
            result_binary += "1"
            result_inv += "0"
        else:
            if default is None:
                raise Exception(f"Invalid State '{state}'")
            else:
                result_binary += str(default)
                result_inv += str(default)
    return result_binary, result_inv


def find_match(lines, pattern, pos):
    print(f"Pos {pos}, lines {len(lines)}")
    return list(filter(lambda l: l[pos] == pattern[pos], lines))


def main(args):
    lines = []
    with open("3.txt", "r") as input_file:
        for line in input_file:
            line_data = line.strip()
            lines += [line_data]
    result_high, result_lower = get_characteristic(lines)
    print(
        f"Result binary: {result_high} x {result_lower} = {int(result_high, 2) * int(result_lower, 2)}")
    match_high = None
    candidates = lines
    for index in range(len(lines[0])):
        print(f"Pattern: {result_high}")
        candidates = find_match(candidates, result_high, index)
        print(f"Candidates: {len(candidates)}")
        if len(candidates) == 1:
            match_high = candidates[0]
            break
        result_high, ignored = get_characteristic(candidates, 1)
    print(f"Match: {match_high}")
    match_low = None
    candidates = lines
    for index in range(len(lines[0])):
        print(f"Pattern: {result_lower}")
        candidates = find_match(candidates, result_lower, index)
        print(f"Candidates: {len(candidates)}")
        if len(candidates) == 1:
            match_low = candidates[0]
            break
        ignored, result_lower = get_characteristic(candidates, 0)
    print(f"Match: {match_low}")
    print(f"Matches: {match_high} x {match_low} = {int(match_low, 2) * int(match_high, 2)}")



if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))
