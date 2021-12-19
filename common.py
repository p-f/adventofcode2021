from typing import TypeVar, Callable

X = TypeVar("X")


def read_tokens(path: str, conv: Callable[[str], X] = lambda x: x) -> list[X]:
    tokens: list[X] = []
    with open(path, "r") as input_file:
        for line in input_file:
            line_data = line.strip()
            for token in line_data.split(","):
                tokens += [conv(token)]
    return tokens
