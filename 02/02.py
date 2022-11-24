def load_data():
    data = []
    with open("02.txt", "r") as f:
        for line in f:
            data.append(line.strip())
    return data


def first():
    commands = load_data()
    horizontal, vertical = 0, 0

    for command in commands:
        dir, num = command.split()
        if dir == "forward":
            horizontal += int(num)
        elif dir == "up":
            vertical -= int(num)
        elif dir == "down":
            vertical += int(num)

    print(horizontal * vertical)


def second():
    commands = load_data()
    horizontal, vertical, aim = 0, 0, 0

    for command in commands:
        dir, num = command.split()
        if dir == "forward":
            horizontal += int(num)
            vertical += int(num) * aim
        elif dir == "up":
            aim -= int(num)
        elif dir == "down":
            aim += int(num)

    print(horizontal * vertical)


if __name__ == '__main__':
    first()
    second()