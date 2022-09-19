"""
    음료수 얼려 먹기
"""
from sys import stdin as input
from collections import deque

GORUND = "1"
WALL = "0"
MOVE = [
    (-1, 0),  # 위
    (0, 1),  # 오른쪽
    (1, 0),  # 아래
    (0, -1),  # 왼쪽
]

input = open('./test/original.txt')
ROW, COL = map(int, input.readline().split())
ROW_END, ROW_COL = ROW - 1, COL - 1
BOREAD = [list(input.readline().strip()) for _ in range(ROW)]


class D:
    visited = [[0] * COL for _ in range(ROW)]


def bfs(row: int, col: int) -> int:
    q = deque([(row, col, 1)])

    while q:
        crow, ccol, ccount = q.popleft()
        if D.visited[crow][ccol]:
            continue
        D.visited[crow][ccol] = ccount

        for trow, tcol in MOVE:
            nrow, ncol = trow + crow, tcol + ccol
            if not (0 <= nrow < ROW and 0 <= ncol < COL):
                continue
            if BOREAD[nrow][ncol] == WALL:
                continue
            if D.visited[nrow][ncol]:
                continue
            q.append((nrow, ncol, ccount + 1))


def main() -> None:
    """ 실행 """

    for row in range(ROW):
        for col in range(COL):
            if BOREAD[row][col] == WALL:
                continue
            if D.visited[row][col]:
                continue
            bfs(row, col)

    print(D.visited[ROW_END][ROW_COL])


if __name__ == '__main__':
    main()
