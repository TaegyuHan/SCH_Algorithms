from sys import stdin as input

input = open('./test/original.txt')

position = input.readline()


def main():
    COL = {alpha: idx + 1 for idx, alpha in enumerate(["a", "b", "c", "d", "e", "f", "g", "h"])}
    BOARD_MAX = 8
    NIGHT_MOVE = [
        (-2, -1),  # 왼쪽 위 1
        (-1, -2),  # 왼쪽 위 2
        (-2, 1),  # 오른쪽 위 1
        (-1, 2),  # 오른쪽 위 2
        (1, -2),  # 왼쪽 아래 1
        (2, -1),  # 왼쪽 아래 2
        (1, 2),  # 오른쪽 아래 1
        (2, 1),  # 오른쪽 아래 2
    ]

    answer = 0

    col, row = position[0], position[1]
    crow, ccol = int(row), COL[col]

    for trow, tcol in NIGHT_MOVE:
        nrow, ncol = crow + trow, ccol + tcol
        if not (1 <= nrow <= BOARD_MAX and 1 <= ncol <= BOARD_MAX):
            continue
        answer += 1
    print(answer)


if __name__ == '__main__':
    main()
