def load_data():
    with open("07.txt", "r") as f:
        data = f.readline().split(",")
    return list(map(int, data))


def first(data):
    left, right = min(data), max(data)
    fuels = []
    for pos in range(left, right + 1):
        fuel = 0
        for crab in data:
            fuel += abs(crab - pos)
        fuels.append(fuel)
    return min(fuels)


def fuel_cost(crab, pos):
    return abs(crab - pos) * (abs(crab - pos) + 1) // 2


def second(data):
    left, right = min(data), max(data)
    fuels = []
    for pos in range(left, right + 1):
        fuel = 0
        for crab in data:
            fuel += fuel_cost(crab, pos)
        fuels.append(fuel)
    return min(fuels)


if __name__ == '__main__':
    data = load_data()
    print(first(data))
    print(second(data))