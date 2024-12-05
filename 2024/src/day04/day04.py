WORD_TO_FIND = 'XMAS'
WORD_TO_FIND_REVERSED = 'SAMX'


def get_data(filename):
    with open(filename) as f:
        data = []
        for row, line in enumerate(f.readlines()):
            data.append([])
            for ch in line:
                data[row].append(ch)

        return data


def is_horizontal_xmas_forward(data, row, col, width, height):
    if col + 4 > width:
        return False
    
    return ''.join(data[row][col : col + 4]) == WORD_TO_FIND

def is_horizontal_xmas_back(data, row, col, width, height):
    if col < 3:
        return False

    return ''.join(data[row][col - 3 : col + 1]) == WORD_TO_FIND_REVERSED

def is_vertical_xmas_up(data, row, col, width, height):
    if row < 3:
        return False

    return "".join(data[r][col] for r in range(row - 3, row+1)) == WORD_TO_FIND_REVERSED

def is_vertical_xmas_down(data, row, col, width, height):
    if row + 4 > height:
        return False

    return "".join(data[r][col] for r in range(row, row + 4)) == WORD_TO_FIND


def is_diagonal_xmas_sw(data, row, col, width, height):
    if col < 3 or row + 4 > height:
        return False

    diagonal_word = "".join(data[row + i][col - i] for i in range(4))
    return diagonal_word == WORD_TO_FIND


def is_diagonal_xmas_nw(data, row, col, width, height):
    if col < 3 or row < 3:
        return False

    diagonal_word = "".join(data[row - i][col - i] for i in range(4))
    return diagonal_word == WORD_TO_FIND


def is_diagonal_xmas_se(data, row, col, width, height):
    if col + 4 > width or row + 4 > height:
        return False

    diagonal_word = "".join(data[row + i][col + i] for i in range(4))
    return diagonal_word == WORD_TO_FIND


def is_diagonal_xmas_ne(data, row, col, width, height):
    if col + 4 > width or row < 3:
        return False

    diagonal_word = "".join(data[row - i][col + i] for i in range(4))
    return diagonal_word == WORD_TO_FIND


def solve_p1():
    data = get_data('input.txt')
    width, height = len(data[0]), len(data)
    result = 0

    for row in range(height):
        for col in range(width):
            current_char = data[row][col]
            if current_char == WORD_TO_FIND[0]:
                if is_horizontal_xmas_forward(data, row, col, width, height):
                    result += 1
                if is_horizontal_xmas_back(data, row, col, width, height):
                    result += 1
                if is_vertical_xmas_up(data, row, col, width, height):
                    result += 1
                if is_vertical_xmas_down(data, row, col, width, height):
                    result += 1
                if is_diagonal_xmas_sw(data, row, col, width, height):
                    result += 1
                if is_diagonal_xmas_nw(data, row, col, width, height):
                    result += 1
                if is_diagonal_xmas_se(data, row, col, width, height):
                    result += 1
                if is_diagonal_xmas_ne(data, row, col, width, height):
                    result += 1

    return result


if __name__ == "__main__":
    print("Answer part 1: {}".format(solve_p1()))
