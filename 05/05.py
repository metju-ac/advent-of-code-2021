def load_data():
    data = []
    with open("05.txt", "r") as f:
        for line in f:
            cur_line = line.replace(" -> ", ",").split(",")
            data.append(list(map(int, cur_line)))
    return data


def get_size(data):
    max_x, max_y = 0, 0
    for row in data:
        x1, y1, x2, y2 = row
        max_x = max(max(x1, x2), max_x)
        max_y = max(max(y1, y2), max_y)
    return max_x + 1, max_y + 1


def get_hor_ver_lines(data):
    lines = []
    for row in data:
        x1, y1, x2, y2 = row
        if x1 == x2 or y1 == y2:
            lines.append(row)
    return lines


def get_diagonal_lines(data):
    lines = []
    for row in data:
        x1, y1, x2, y2 = row
        if abs(x1 - x2) == abs(y1 - y2):
            lines.append(row)
    return lines


def write_hor_ver_lines(diagram, lines):
    for line in lines:
        x1, y1, x2, y2 = line
        for x in range(min(x1, x2), max(x1, x2) + 1):
            for y in range(min(y1, y2), max(y1, y2) + 1):
                diagram[y][x] += 1


def write_diagonal_lines(diagram, lines):
    for line in lines:
        x1, y1, x2, y2 = line
        x, y = x1, y1

        while x != x2:
            diagram[y][x] += 1
            if x2 > x1:
                x += 1
            else:
                x -= 1

            if y2 > y1:
                y += 1
            else:
                y -= 1

        diagram[y][x] += 1


def count_overlaps(diagram):
    count = 0
    for row in diagram:
        for col in row:
            if col >= 2:
                count += 1
    return count


def first(data):
    max_x, max_y = get_size(data)
    lines = get_hor_ver_lines(data)
    diagram = [[0 for _ in range(max_x)] for _ in range(max_y)]

    write_hor_ver_lines(diagram, lines)
    return count_overlaps(diagram)


def second(data):
    max_x, max_y = get_size(data)
    hor_ver_lines = get_hor_ver_lines(data)
    diagonal_lines = get_diagonal_lines(data)
    diagram = [[0 for _ in range(max_x)] for _ in range(max_y)]

    write_hor_ver_lines(diagram, hor_ver_lines)
    write_diagonal_lines(diagram, diagonal_lines)
    return count_overlaps(diagram)


if __name__ == '__main__':
    data = load_data()
    print(first(data))
    print(second(data))
