def load_data():
    data = []
    with open("11.txt", "r") as f:
        for line in f:
            chars = [c for c in line.strip()]
            nums = list(map(int, chars))
            data.append(nums)
    return data


def increase_energy(octopuses):
    for row in range(10):
        for col in range(10):
            octopuses[row][col] += 1


def reset_energy(octopuses):
    for row in range(10):
        for col in range(10):
            if octopuses[row][col] > 9:
                octopuses[row][col] = 0


def get_charged(octopuses):
    charged = []
    for row in range(10):
        for col in range(10):
            if octopuses[row][col] == 10:
                charged.append((row, col))
    return charged


def get_neighbours(row, col):
    neighbours = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            neighbours.append((row + i, col + j))
    return neighbours


def charge_neighbours(octopuses, r, c):
    new_charged = []
    neighbours = get_neighbours(r, c)
    for row, col in neighbours:
        if row < 0 or row > 9 or col < 0 or col > 9:
            continue
        octopuses[row][col] += 1
        if octopuses[row][col] == 10:
            new_charged.append((row, col))
    return new_charged


def step(octopuses):
    flashes = 0
    increase_energy(octopuses)
    charged = get_charged(octopuses)

    while charged:
        flashes += 1
        row, col = charged.pop()
        new_charged = charge_neighbours(octopuses, row, col)
        charged += new_charged

    reset_energy(octopuses)
    return flashes


def first(octopuses):
    flashes = 0
    for _ in range(100):
        flashes += step(octopuses)
    return flashes


def second(octopuses):
    count = 0
    while True:
        count += 1
        flashes = step(octopuses)
        if flashes == 100:
            return count


if __name__ == '__main__':
    data = load_data()
    print(first(data))
    data = load_data()
    print(second(data))
