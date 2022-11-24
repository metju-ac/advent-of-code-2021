def load_data():
    data = []
    with open("09.txt", "r") as f:
        for line in f:
            chars = [c for c in line.strip()]
            nums = list(map(int, chars))
            data.append(nums)
    return data


def get_neighbours(heightmap, row, col):
    neighbours = []
    if row > 0:
        neighbours.append(heightmap[row - 1][col])
    if row < len(heightmap) - 1:
        neighbours.append(heightmap[row + 1][col])
    if col > 0:
        neighbours.append(heightmap[row][col - 1])
    if col < len(heightmap[0]) - 1:
        neighbours.append(heightmap[row][col + 1])
    return neighbours


def first(heightmap):
    res = 0

    for row in range(len(heightmap)):
        for col in range(len(heightmap[0])):
            height = heightmap[row][col]
            neighbours = get_neighbours(heightmap, row, col)
            if height < min(neighbours):
                res += height + 1

    return res


def flood_fill(heightmap, row, col, count):
    if row < 0 or row >= len(heightmap) or col < 0 or col >= len(heightmap[0]):
        return count
    if heightmap[row][col] == 9 or heightmap[row][col] == -1:
        return count

    heightmap[row][col] = -1
    count += 1

    count = flood_fill(heightmap, row - 1, col, count)
    count = flood_fill(heightmap, row + 1, col, count)
    count = flood_fill(heightmap, row, col - 1, count)
    count = flood_fill(heightmap, row, col + 1, count)

    return count


def second(heightmap):
    basins = []
    for row in range(len(heightmap)):
        for col in range(len(heightmap[0])):
            basin = flood_fill(heightmap, row, col, 0)
            if basin > 0:
                basins.append(basin)

    largest = sorted(basins)[-3:]
    return largest[0] * largest[1] * largest[2]


if __name__ == '__main__':
    data = load_data()
    print(first(data))
    print(second(data))
