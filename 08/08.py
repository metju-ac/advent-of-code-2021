# Could be done much easier

def load_data():
    data = []
    with open("08.txt", "r") as f:
        for line in f:
            patterns, output = line.strip().replace(" | ", "|").split("|")
            data.append([patterns.split(" "), output.split(" ")])
    return data


def first(data):
    count = 0
    for entry in data:
        for output in entry[1]:
            if len(output) in [2, 3, 4, 7]:
                count += 1
    return count


def count_occurrences(paterns):
    occurrences = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0}

    for pattern in paterns:
        for char in pattern:
            occurrences[char] += 1
    return occurrences


def chars_to_nums(chars):
    chars = chars.replace("a", "0")
    chars = chars.replace("b", "1")
    chars = chars.replace("c", "2")
    chars = chars.replace("d", "3")
    chars = chars.replace("e", "4")
    chars = chars.replace("f", "5")
    chars = chars.replace("g", "6")
    return chars


def get_four(patterns):
    for pattern in patterns:
        if len(pattern) == 4:
            return chars_to_nums(pattern)


def get_mapping(entry):
    occurrences = count_occurrences(entry[0])

    # 0 = a, 1 = b, 2 = c, 3 = d, 4 = e, 5 = f, 6 = g
    b = list(occurrences.values()).index(6)
    e = list(occurrences.values()).index(4)
    f = list(occurrences.values()).index(9)

    a_or_c1 = list(occurrences.values()).index(8)
    a_or_c2 = list(occurrences.values()).index(8, a_or_c1 + 1)

    d_or_g1 = list(occurrences.values()).index(7)
    d_or_g2 = list(occurrences.values()).index(7, d_or_g1 + 1)

    four = get_four(entry[0])
    if str(a_or_c1) in four:
        c = a_or_c1
        a = a_or_c2
    else:
        c = a_or_c2
        a = a_or_c1

    if str(d_or_g1) in four:
        d = d_or_g1
        g = d_or_g2
    else:
        d = d_or_g2
        g = d_or_g1

    return [a, b, c, d, e, f, g]


def get_digit(output, mapping):
    zero = {0, 1, 2, 4, 5, 6}
    one = {2, 5}
    two = {0, 2, 3, 4, 6}
    three = {0, 2, 3, 5, 6}
    four = {1, 2, 3, 5}
    five = {0, 1, 3, 5, 6}
    six = {0, 1, 3, 4, 5, 6}
    seven = {0, 2, 5}
    eight = {0, 1, 2, 3, 4, 5, 6}
    nine = {0, 1, 2, 3, 5, 6}

    digit = set()
    for char in chars_to_nums(output):
        digit.add(mapping.index(int(char)))

    if digit == zero:
        return 0
    elif digit == one:
        return 1
    elif digit == two:
        return 2
    elif digit == three:
        return 3
    elif digit == four:
        return 4
    elif digit == five:
        return 5
    elif digit == six:
        return 6
    elif digit == seven:
        return 7
    elif digit == eight:
        return 8
    elif digit == nine:
        return 9


def get_number(entry, mapping):
    res = 0
    for output in entry[1]:
        res *= 10
        res += get_digit(output, mapping)
    return res


def second(data):
    res = 0
    for entry in data:
        mapping = get_mapping(entry)
        res += get_number(entry, mapping)
    return res


if __name__ == '__main__':
    data = load_data()
    print(first(data))
    print(second(data))