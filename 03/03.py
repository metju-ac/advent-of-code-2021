def load_data():
    data = []
    with open("03.txt", "r") as f:
        for line in f:
            data.append(line.strip())
    return data


def bits(data):
    bits = [0 for i in range(len(data[0]))]

    for line in data:
        for i in range(len(data[0])):
            if line[i] == "1":
                bits[i] += 1
            else:
                bits[i] -= 1

    return bits


def first():
    data = load_data()
    cur_bits = bits(data)

    cur_bits.reverse()
    gamma, epsilon = 0, 0
    base = 1

    for i in range(12):
        if cur_bits[i] > 0:
            gamma += base
        else:
            epsilon += base
        base *= 2

    print(gamma * epsilon)


def load_oxygen_co2(oxygen):
    data = load_data()
    cur_bit = 0

    while len(data) != 1:
        cur_bits = bits(data)
        new_data = []
        most_common = "1" if cur_bits[cur_bit] >= 0 else "0"

        for line in data:
            if (line[cur_bit] == most_common and oxygen) or (line[cur_bit] != most_common and not oxygen):
                new_data.append(line)

        data = new_data
        cur_bit += 1

    res, base = 0, 1
    for i in range(len(data[0])):
        if data[0][-i - 1] == "1":
            res += base
        base *= 2

    print(res)
    return res


def second():
    print(load_oxygen_co2(True) * load_oxygen_co2(False))


if __name__ == '__main__':
    first()
    second()
