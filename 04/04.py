class Board:
    def __init__(self, rows):
        self.rows = rows
        self.unmarked_sum = 0
        for row in rows:
            self.unmarked_sum += sum(row)

    def find_number(self, number):
        for row in range(5):
            for col in range(5):
                if self.rows[row][col] == number:
                    return row, col
        return -1, -1

    def mark_number(self, number):
        row, col = self.find_number(number)
        if row == -1:
            return
        self.unmarked_sum -= self.rows[row][col]
        self.rows[row][col] = -1

    def is_won(self):
        for row in self.rows:
            if sum(row) == -5:
                return True

        for col in range(5):
            col_sum = 0
            for row in range(5):
                col_sum += self.rows[row][col]
            if col_sum == -5:
                return True


def load_data():
    data = []
    with open("04.txt", "r") as f:
        for line in f:
            data.append(line.strip())
    return data


def initialize(data):
    first_row = data[0].split(",")
    chosen_numbers = list(map(int, first_row))
    created_boards = []

    i = 2
    while i < len(data):
        rows = []
        for _ in range(5):
            cur_row = data[i].replace("  ", " ").split(" ")
            rows.append(list(map(int, cur_row)))
            i += 1
        created_boards.append(Board(rows))
        i += 1

    return chosen_numbers, created_boards


def first(chosen_numbers, boards):
    for cur_num in chosen_numbers:
        for board in boards:
            board.mark_number(cur_num)
            if board.is_won():
                return board.unmarked_sum * cur_num


def second(chosen_numbers, boards):
    boards_left = len(boards)
    for cur_num in chosen_numbers:
        for i, board in enumerate(boards):
            if board is None:
                continue
            board.mark_number(cur_num)
            if board.is_won():
                boards_left -= 1
                boards[i] = None
                if boards_left == 0:
                    return board.unmarked_sum * cur_num



if __name__ == '__main__':
    data = load_data()
    numbers, boards = initialize(data)
    print(first(numbers, boards))
    print(second(numbers, boards))

