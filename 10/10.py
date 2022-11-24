from collections import deque


def load_data():
    data = []
    with open("10.txt", "r") as f:
        for line in f:
            chars = [c for c in line.strip()]
            data.append(chars)
    return data


def matches(opener, closer):
    return (opener == "(" and closer == ")") or \
           (opener == "[" and closer == "]") or \
           (opener == "{" and closer == "}") or \
           (opener == "<" and closer == ">")


def get_score(char):
    scores = {")": 3, "]": 57, "}": 1197, ">": 25137,
              "(": 1, "[": 2, "{": 3, "<": 4}
    return scores[char]


def solve_corrupter_line(line):
    stack = deque()
    for char in line:
        if char in {"(", "[", "{", "<"}:
            stack.append(char)
            continue
        opener = stack.pop()
        if not matches(opener, char):
            return get_score(char)
    return 0


def first(lines):
    res = 0
    for line in lines:
        res += solve_corrupter_line(line)
    return res


def filter_lines(lines):
    res = []
    for line in lines:
        if solve_corrupter_line(line) == 0:
            res.append(line)
    return res


def solve_incomplete_line(line):
    score = 0
    stack = deque()
    for char in line:
        if char in {"(", "[", "{", "<"}:
            stack.append(char)
        else:
            stack.pop()

    while stack:
        score *= 5
        score += get_score(stack.pop())
    return score


def second(lines):
    scores = []
    lines = filter_lines(lines)

    for line in lines:
        scores.append(solve_incomplete_line(line))
    return sorted(scores)[len(scores) // 2]


if __name__ == '__main__':
    data = load_data()
    print(first(data))
    print(second(data))
