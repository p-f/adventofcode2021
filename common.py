from typing import TypeVar, Callable, Optional

X = TypeVar("X")


def read_blocks(path: str) -> list[list[str]]:
    blocks: list[list[str]] = []
    current_block: list[str] = []
    with open(path, "r") as input_file:
        for line in input_file:
            line_data = line.strip()
            if len(line_data) == 0:
                if len(current_block) > 0:
                    blocks += [current_block]
                    current_block = []
                continue
            current_block += [line_data]
        if len(current_block) > 0:
            blocks += [current_block]
    return blocks


def read_tokens(path: str, conv: Callable[[str], X] = lambda x: x) -> list[X]:
    tokens: list[X] = []
    with open(path, "r") as input_file:
        for line in input_file:
            tokens += split_tokens(line, ",", conv)
    return tokens


def split_tokens(line: str, delim: Optional[str] = None,
                 conv: Callable[[str], X] = lambda x: x) -> list[X]:
    tokens: list[X] = []
    for token in line.strip().split(delim):
        tokens += [conv(token)]
    return tokens
