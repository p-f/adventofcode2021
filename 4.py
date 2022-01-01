import functools

from common import read_blocks, split_tokens


class Board:

    def __init__(self):
        self.data = []
        for _ in range(5):
            line = []
            for _ in range(5):
                line += [[0, False]]
            self.data.append(line)

    def get_row(self, nr):
        return self.data[nr]

    def get_col(self, nr):
        return [self.data[i][nr] for i in range(5)]

    def set_row(self, nr, data):
        assert len(data) == 5
        for i in range(5):
            self.data[nr][i][0] = data[i]

    @staticmethod
    def check_bingo(data_row):
        for item in data_row:
            if not item[1]:
                return False
        return True

    def mark(self, number):
        res = False
        for row in self.data:
            for col_nr, cell in enumerate(row):
                if cell[0] == number:
                    cell[1] = True
                if self.check_bingo(row) or \
                        self.check_bingo(self.get_col(col_nr)):
                    res = True
        return res

    def unmarked_sum(self):
        sum_cells = 0
        for row in self.data:
            for cell in row:
                if not cell[1]:
                    sum_cells += cell[0]
        return sum_cells

    def reset(self):
        for row in self.data:
            for cell in row:
                cell[1] = False

    def __str__(self) -> str:
        linedata = []
        for line in self.data:
            linedata.append("\t".join(map(lambda x: x.__str__(), line)))
        return "\n".join(linedata)


def parse_board(data: list[str]) -> Board:
    assert len(data) == 5
    board = Board()
    for i in range(5):
        board.set_row(i, split_tokens(data[i], conv=int))
    return board


def main(args):
    data = read_blocks("4.txt")
    numbers = split_tokens(data[0][0], ",", int)
    print("Numbers: ", numbers)
    boards: list[Board] = []
    for board_data in data[1:]:
        board = parse_board(board_data)
        boards.append(board)
    for number in numbers:
        done = False
        for board in boards:
            if board.mark(number):
                print(f"Bingo on board: \n{board}\n")
                sum_b = board.unmarked_sum()
                print(f"Sum: {sum_b} x {number} -> {sum_b * number}")
                done = True
                break
        if done:
            break
    # Second strategy:
    for board in boards:
        board.reset()
    winners = []
    boards_to_test = list(boards)
    already_won = []
    for _ in range(len(boards_to_test)):
        already_won.append(False)
    while not functools.reduce(lambda x, y: x and y, already_won):
        for number in numbers:
            for nr, board in enumerate(boards_to_test):
                if already_won[nr]:
                    continue
                if board.mark(number):
                    score = number * board.unmarked_sum()
                    print(
                        f"Board won for {number} with score {score}:\n{board}\n")
                    winners.append(score)
                    already_won[nr] = True
                    print(f"Left to test {len(boards_to_test)}")
    print(f"Score of last winner: {winners[-1]}")


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))
