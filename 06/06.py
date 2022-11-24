def load_data():
    with open("06.txt", "r") as f:
        data = f.readline().split(",")
    return list(map(int, data))


def first(fishes):
    for _ in range(80):
        new_fishes = []
        for fish in fishes:
            if fish == 0:
                new_fishes.append(6)
                new_fishes.append(8)
            else:
                new_fishes.append(fish - 1)
        fishes = new_fishes
    return len(fishes)


def get_ages(fishes):
    ages = [0 for _ in range(9)]
    for fish in fishes:
        ages[fish] += 1
    return ages


def second(fishes):
    ages = get_ages(fishes)
    for _ in range(256):
        new_ages = [0 for _ in range(9)]

        new_ages[0] = ages[1]
        new_ages[1] = ages[2]
        new_ages[2] = ages[3]
        new_ages[3] = ages[4]
        new_ages[4] = ages[5]
        new_ages[5] = ages[6]
        new_ages[6] = ages[7]
        new_ages[7] = ages[8]
        new_ages[8] = ages[0]
        new_ages[6] += ages[0]

        ages = new_ages

    return sum(ages)


if __name__ == '__main__':
    fishes = load_data()
    print(first(fishes))
    print(second(fishes))
