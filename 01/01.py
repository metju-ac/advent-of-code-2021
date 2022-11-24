def load_data():
    data = []
    with open("01.txt", "r") as f:
        for line in f:
            data.append(int(line.strip()))
    return data


def first():
    depths = load_data()
    count = 0
    for i in range(1, len(depths)):
        if depths[i] > depths[i - 1]:
            count += 1
    print(count)


def second():
    depths = load_data()
    count = 0
    for i in range(3, len(depths)):
        if depths[i] > depths[i - 3]:
            count += 1
    print(count)


if __name__ == '__main__':
    first()
    second()

